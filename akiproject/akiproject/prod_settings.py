from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-!c-pnku_!1hi8&eu20vgasd8hAS7$@9tfdohhg=0fl0c4r^2l'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '206.189.105.19']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aki_db',
        'USER': 'aki_db_user',
        'PASSWORD': '21aki_creativ',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [ STATIC_DIR ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')