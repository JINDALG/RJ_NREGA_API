from celery import shared_task

from api.models import Work


@shared_task
def pay():
    Work.objects.filter(payment_done=False, verified_by__isnull=False).update(payment_done=True)
