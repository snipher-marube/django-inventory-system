from .base import *

# debug mode
DEBUG = True

# aLLOWED HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email Backend for Testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# staticfiles
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]