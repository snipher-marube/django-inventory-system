import os
from celery import Celery
from django.conf import settings

# set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings.development')

# create a celery instance
app = Celery('inventory_system')

# Load task modules from all registered Django apps
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-discover tasks in all registered django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'request: {self.request!r}')