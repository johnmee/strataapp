# Strata Properties

A Django web application for strata management software.

- **Business Plan**: https://www.strata.properties/business_plan.html
- **Roadmap**: https://www.strata.properties/roadmap.html
- **Blog**: https://www.strata.properties/blog/

## Technology Stack

- **Backend**: Django 6.0 with Python
- **ASGI Server**: Uvicorn
- **Web Server**: nginx
- **Database**: SQLite (development), PostgreSQL (recommended for production)
- **Hosting**: Linux VPS with systemd

## Prerequisites

- Python 3.8+
- pip
- nginx
- Uvicorn

## Local Development

### Setup

```bash
cd app/strataapp
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root (not committed to git):

```
SECRET_KEY=your-dev-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Or set them in your shell:

```bash
export SECRET_KEY="dev-key"
export DEBUG=True
export ALLOWED_HOSTS="localhost,127.0.0.1"
```

### Running Locally

```bash
cd app/strataapp
python manage.py runserver
```

Visit http://localhost:8000

## Project Structure

```
strataapp/
├── app/strataapp/               # Django project
│   ├── strataapp/               # Project config
│   │   ├── settings.py          # Django settings
│   │   ├── asgi.py              # ASGI entry point
│   │   └── urls.py              # URL routing
│   ├── home/                    # Home app
│   │   ├── views.py             # View functions
│   │   └── templates/           # HTML templates
│   └── manage.py                # Django management
├── blog/                        # Blog submodule
├── strataapp.nginx              # nginx configuration
├── strataapp.service            # systemd service file
├── strataapp.env.example        # Environment variables template
└── README.md
```

## Production Deployment

### Prerequisites

- VPS with root access
- Domain configured (www.strata.properties)
- SSL certificate (Certbot/Let's Encrypt configured)

### Step 1: Install Dependencies

```bash
# On your VPS
apt update
apt install python3 python3-pip nginx
pip3 install uvicorn django
```

### Step 2: Create Environment File

```bash
sudo mkdir -p /etc/strataapp
sudo nano /etc/strataapp/strataapp.env
```

Add:

```
SECRET_KEY=<generated-secret-key>
DEBUG=False
ALLOWED_HOSTS=www.strata.properties,strata.properties
```

Set permissions:

```bash
sudo chmod 600 /etc/strataapp/strataapp.env
sudo chown www-data:www-data /etc/strataapp/strataapp.env
```

### Step 3: Install Systemd Service

```bash
sudo cp strataapp.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable strataapp
sudo systemctl start strataapp
```

### Step 4: Configure nginx

```bash
sudo cp strataapp.nginx /etc/nginx/sites-available/strataapp
sudo ln -s /etc/nginx/sites-available/strataapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 5: Verify

```bash
sudo systemctl status strataapp
# Check logs
sudo journalctl -u strataapp -f
# Test nginx
curl https://www.strata.properties/
```

## Managing the Application

### View Logs

```bash
sudo journalctl -u strataapp -f
```

### Restart After Code Changes

```bash
sudo systemctl restart strataapp
```

### Stop/Start

```bash
sudo systemctl stop strataapp
sudo systemctl start strataapp
```

## Blog

The blog is a git submodule. To update it:

```bash
git submodule update --remote
git commit -am "Update blog"
git push
```

The blog is served from `/blog/` and rebuilt on each deploy.

## Development Notes

- Settings are loaded from environment variables for security
- Never commit production secrets to git
- Use `strataapp.env.example` as a template for production environment files
- The ASGI application supports WebSockets if needed in the future
