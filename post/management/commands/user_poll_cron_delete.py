import datetime
from django.core.management.base import BaseCommand

from post.models import UserPoll


class Command(BaseCommand):
    help = 'Удаление старых user-poll'

    def handle(self, *args, **kwargs):
        polls = UserPoll.objects.all()
        for poll in polls:
            if (datetime.datetime.today() - poll.created_at) > datetime.timedelta(minutes=7):
                print(f'delete poll from {poll.created_at}')
                poll.delete()
