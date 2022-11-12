from django.apps import AppConfig


class BookVoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_vote'
    verbose_name = 'Голосования за книги'
