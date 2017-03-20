from celery import shared_task

from api.models import Work


@shared_task
def pay():
    pass
