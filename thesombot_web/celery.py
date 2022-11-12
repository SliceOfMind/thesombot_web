import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thesombot_web.settings')

app = Celery('thesombot_web')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# from django_celery_beat.models import PeriodicTask, IntervalSchedule
#
# # executes every 10 seconds.
# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=10,
#     period=IntervalSchedule.SECONDS,
# )
#
# PeriodicTask.objects.create(
#     interval=schedule,
#     name='Importing contacts',
#     task='post.tasks.import_contacts',
# )
