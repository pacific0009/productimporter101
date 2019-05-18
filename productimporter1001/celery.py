import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productimporter1001.settings')

app = Celery('productimporter1001')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()