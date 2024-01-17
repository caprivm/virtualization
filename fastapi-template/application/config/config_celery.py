from celery import Celery
import os
import logging

logging.info("Starting celery worker")

app = Celery(
    "worker",
    broker=os.getenv("CELERY_BROKER_URL", "amqp://rabbitmq:5672"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "mongodb://mongodb:27017"),
    include=["models.model_celery_tasks"],
)

app.conf.update(
    accept_content=["json"],
    result_expires=3600,
    result_serializer="json",
    result_accept_content=["json"],
    task_soft_time_limit=43200,
    task_serializer="json",
    task_track_started=True,
    timezone="America/Bogota",
)

app.autodiscover_tasks()

app.conf.task_routes = {
    "models.model_celery_tasks.*": {"queue": "celery"},
}
