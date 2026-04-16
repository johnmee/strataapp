# Production Deployment

## Architecture

```
Internet
  └── nginx (port 443, SSL, Certbot)
        ├── /        → Uvicorn (127.0.0.1:8000) → Django
        └── /blog/   → blog/public/ (static files, built by GitHub Actions)
```

- **Server**: Linux VPS (BinaryLane)
- **SSH**: Non-standard port (check `/etc/ssh/sshd_config` on the server)
- **User**: `strataapp` system user, home at `/opt/strataapp`
- **Repo**: `/opt/strataapp/repo`
- **Venv**: `/opt/strataapp/repo/app/.venv` (managed by uv)
- **uv**: `/opt/strataapp/.local/bin/uv`
- **Env file**: `/opt/strataapp/strataapp.env`

## First-Time Server Setup

### 1. Create the system user

```bash
sudo useradd -r -d /opt/strataapp -s /bin/bash strataapp
sudo mkdir -p /opt/strataapp
sudo chown strataapp:strataapp /opt/strataapp
```

### 2. Install uv

```bash
sudo -u strataapp bash -c 'curl -LsSf https://astral.sh/uv/install.sh | sh'
```

uv installs to `/opt/strataapp/.local/bin/uv`.

### 3. Create SSH deploy key

```bash
sudo -u strataapp mkdir -p /opt/strataapp/.ssh
sudo -u strataapp chmod 700 /opt/strataapp/.ssh
sudo -u strataapp ssh-keygen -t ed25519 -f /opt/strataapp/.ssh/id_ed25519 -N "" -C "strataapp-deploy"
```

Add the public key (`/opt/strataapp/.ssh/id_ed25519.pub`) to the GitHub repo as a **read-only deploy key**:
GitHub → repo → Settings → Deploy keys → Add deploy key.

Pre-populate known_hosts:

```bash
for f in /etc/ssh/ssh_host_*_key.pub; do echo "github.com $(cat $f)"; done
# The above is wrong — run this instead:
sudo -u strataapp ssh-keyscan github.com > /opt/strataapp/.ssh/known_hosts
sudo chmod 644 /opt/strataapp/.ssh/known_hosts
```

Create SSH config at `/opt/strataapp/.ssh/config`:

```
Host github.com
    IdentityFile    /opt/strataapp/.ssh/id_ed25519
    User            git
    UserKnownHostsFile /opt/strataapp/.ssh/known_hosts
```

### 4. Clone the repository

```bash
sudo -u strataapp GIT_SSH_COMMAND="ssh -F /opt/strataapp/.ssh/config" \
    git clone git@github.com:johnmee/strataapp.git /opt/strataapp/repo
```

### 5. Install Python dependencies

```bash
cd /opt/strataapp/repo/app
sudo -u strataapp /opt/strataapp/.local/bin/uv sync
```

### 6. Create the environment file

```bash
sudo mkdir -p /opt/strataapp
sudo nano /opt/strataapp/strataapp.env
```

Contents (see `strataapp.env.example` for the template):

```
SECRET_KEY=<generate with: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())">
DEBUG=False
ALLOWED_HOSTS=www.strata.properties,strata.properties
```

Set permissions:

```bash
sudo chown root:strataapp /opt/strataapp/strataapp.env
sudo chmod 640 /opt/strataapp/strataapp.env
```

### 7. Install the systemd service

```bash
sudo cp /opt/strataapp/repo/strataapp.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable strataapp
sudo systemctl start strataapp
```

Allow the strataapp user to restart the service without a password:

```bash
echo 'strataapp ALL=(ALL) NOPASSWD: /bin/systemctl restart strataapp' \
    | sudo tee /etc/sudoers.d/strataapp
```

### 8. Configure nginx

```bash
sudo cp /opt/strataapp/repo/strataapp.nginx /etc/nginx/sites-available/strataapp
sudo ln -s /etc/nginx/sites-available/strataapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 9. SSL certificate (Certbot)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d www.strata.properties -d strata.properties
```

Certbot edits the nginx config automatically. Renewal is handled by a systemd timer installed by Certbot.

### 10. Set up GitHub Actions secrets

In GitHub → repo → Settings → Secrets → Actions, add:

| Secret | How to get the value |
|---|---|
| `DEPLOY_HOST` | Server hostname or IP |
| `DEPLOY_PORT` | SSH port (`grep Port /etc/ssh/sshd_config`) |
| `DEPLOY_USER` | `strataapp` |
| `DEPLOY_SSH_KEY` | Generate a new key: `ssh-keygen -t ed25519 -f /tmp/actions_deploy -N ""`; paste private key here; add public key to `/opt/strataapp/.ssh/authorized_keys` |
| `DEPLOY_KNOWN_HOSTS` | Run on server: `for f in /etc/ssh/ssh_host_*_key.pub; do echo "[HOSTNAME]:PORT $(cat $f)"; done` (replace HOSTNAME and PORT) |

## Deploying

Deployment is automatic on every push to `main` via GitHub Actions (`.github/workflows/deploy.yml`).

The workflow:
1. Checks out the repo
2. Builds the blog with Hugo
3. Rsyncs `blog/public/` to the server
4. SSHs into the server, runs `git pull` and `uv sync`
5. Restarts the `strataapp` systemd service

**Never edit files directly in `/opt/strataapp/repo/` on the server.** All changes must go through git — a direct edit will cause `git pull` to fail on the next deploy.

## Managing the Service

```bash
# Status
sudo systemctl status strataapp

# Logs (live)
sudo journalctl -u strataapp -f

# Last 50 log lines
sudo journalctl -u strataapp -n 50

# Restart manually
sudo systemctl restart strataapp
```

## nginx Logs

```bash
tail -f /var/log/nginx/strataapp-access.log
tail -f /var/log/nginx/strataapp-error.log
```

## File Permissions Reference

| Path | Owner | Mode | Purpose |
|---|---|---|---|
| `/opt/strataapp/` | `strataapp:strataapp` | `755` | App home |
| `/opt/strataapp/.ssh/` | `strataapp:strataapp` | `700` | SSH keys |
| `/opt/strataapp/.ssh/id_ed25519` | `strataapp:strataapp` | `600` | GitHub deploy key |
| `/opt/strataapp/.ssh/authorized_keys` | `strataapp:strataapp` | `600` | GitHub Actions deploy key |
| `/opt/strataapp/repo/` | `strataapp:strataapp` | `755` | Git repository |
| `/opt/strataapp/strataapp.env` | `root:strataapp` | `640` | Production secrets |
| `/etc/systemd/system/strataapp.service` | `root:root` | `644` | Service definition |
| `/etc/nginx/sites-available/strataapp` | `root:root` | `644` | nginx config |
| `/etc/sudoers.d/strataapp` | `root:root` | `440` | Sudo rules |
