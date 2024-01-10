from celery import Celery

app = Celery()
app.autodiscover_tasks()
