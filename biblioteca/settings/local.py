from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER': 'marchena',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


STATIC_URL = 'static/'
