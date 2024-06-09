from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'
