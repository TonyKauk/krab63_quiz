import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krab63_quiz.settings')
app = Celery('krab63_quiz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
