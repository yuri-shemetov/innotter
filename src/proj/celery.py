import os
from celery import Celery
<<<<<<< HEAD
=======
from . import local_settings 
>>>>>>> 6b5f6e454b4fa8840fd8da4e8da5ad329506f2eb


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

<<<<<<< HEAD
app = Celery('proj')
=======
broker = local_settings.CELERY_BROKER_URL
app = Celery('proj', broker=broker)
>>>>>>> 6b5f6e454b4fa8840fd8da4e8da5ad329506f2eb
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
