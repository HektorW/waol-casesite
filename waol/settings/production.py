from .base import *

import dj_database_url
import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'waol_db',
    }
}


DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] =  dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']



try:
    from .local import *
except ImportError:
    pass
