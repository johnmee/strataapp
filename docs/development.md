# Development Setup

## Stack

- **Django 6.0** — web framework (ASGI mode)
- **Uvicorn** — ASGI application server
- **uv** — Python package and virtualenv manager
- **Hugo** — static site generator for the blog
- **SQLite** — database (development only)

## Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Hugo (for blog development only)

## Setup

```bash
git clone git@github.com:johnmee/strataapp.git
cd strataapp/app
uv sync
```

## Running the App

```bash
cd app/strataapp
python manage.py runserver
```

Visit http://localhost:8000

Django's built-in dev server is sufficient for local development — no need to run Uvicorn locally.

## Environment Variables

Django settings are driven by environment variables. In development the defaults are fine:

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `development-secret-key` | Django secret key |
| `DEBUG` | `False` | Enable debug mode |
| `ALLOWED_HOSTS` | `127.0.0.1` | Comma-separated allowed hosts |

To override, export them in your shell before running the server:

```bash
export DEBUG=True
export ALLOWED_HOSTS=localhost,127.0.0.1
python manage.py runserver
```

## Project Structure

```
strataapp/
├── app/
│   ├── strataapp/               # Django project
│   │   ├── strataapp/           # Project config
│   │   │   ├── settings.py      # Settings (reads from env vars)
│   │   │   ├── urls.py          # URL routing
│   │   │   └── asgi.py          # ASGI entry point
│   │   ├── home/                # Home page app
│   │   │   ├── views.py
│   │   │   └── templates/
│   │   │       └── home.html
│   │   └── manage.py
│   └── pyproject.toml           # Python dependencies (managed by uv)
├── blog/                        # Hugo blog (source)
│   ├── content/                 # Blog posts (markdown)
│   ├── layouts/                 # Hugo templates
│   ├── static/                  # Static assets
│   └── hugo.toml                # Hugo config
├── docs/                        # This documentation
├── .github/workflows/           # GitHub Actions CI/CD
├── strataapp.nginx              # nginx config (reference)
├── strataapp.service            # systemd service (reference)
└── strataapp.env.example        # Environment variable template

```

## Blog Development

Install Hugo, then:

```bash
cd blog
hugo server
```

Visit http://localhost:1313

Blog posts are markdown files in `blog/content/posts/`. The `blog/public/` directory is gitignored — it is built by GitHub Actions on deploy and rsynced to the production server.

## Django Apps

New Django apps live under `app/strataapp/`. After creating one:

1. Add it to `INSTALLED_APPS` in `settings.py`
2. Add its URL patterns to `urls.py`
