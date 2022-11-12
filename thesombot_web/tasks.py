# import datetime
#
# from celery import shared_task
#
# from post.models import UserPoll
# from celery.utils.log import get_task_logger
#
#
# logger = get_task_logger(__name__)
#
#
# @shared_task
# def user_poll_delete():
#     polls = UserPoll.objects.all()
#     for poll in polls:
#         if (datetime.datetime.today() - poll.created_at) > datetime.timedelta(minutes=7):
#             logger.info(f'delete poll from {poll.created_at}')
#             poll.delete()
