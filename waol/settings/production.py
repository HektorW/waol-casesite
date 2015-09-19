from .base import *


DEBUG = False
TEMPLATE_DEBUG = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(BASE_DIR, '_db'),
    }
}




try:
    from .local import *
except ImportError:
    pass
