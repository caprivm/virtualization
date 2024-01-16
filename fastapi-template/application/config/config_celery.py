from celery import Celery
import os
import logging

logging.info("Starting celery worker")

app = Celery(
    "worker",
    broker=os.getenv("CELERY_BROKER_URL", "amqp://rabbitmq:5672"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "mongodb://mongodb:27017"),
    include=["models.celery_tasks"],
)

app.conf.update(
    result_expires=3600,
    task_serializer="json",
    task_soft_time_limit=43200,
    accept_content=["pickle", "json"],
    task_track_started=True,
    enable_utc=True,
    timezone="America/Bogota",
)

app.autodiscover_tasks()

app.conf.task_routes = {
    "models.celery_tasks.*": {"queue": "celery"},
}

if __name__ == "__main__":
    app.start()
