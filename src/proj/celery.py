import os
from celery import Celery
from . import local_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

broker = local_settings.CELERY_BROKER_URL
app = Celery('proj', broker=broker)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
