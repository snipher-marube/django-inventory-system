"""
WSGI config for inventory_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from decouple import config
from django.core.wsgi import get_wsgi_application

# set default environment to 'development' if not specified
environment = config('ENVIRONMENT', default='development')

if environment == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings.development')

application = get_wsgi_application()
