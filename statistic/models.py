from django.db import models
from django.urls import reverse


class Statistic(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    # all_subs_counter = models.IntegerField(default=0, verbose_name='Общее количество купивших подписку за все время')
    # no_buy_users_counter = models.IntegerField(default=0, verbose_name='Количество пользователей не купивших подписку')
    # block_users_counter = models.IntegerField(default=0, verbose_name='Количество пользователей заблокировавших бота')
    # archive_books_sum = models.IntegerField(default=0, verbose_name='Сумма покупок книг из архива')
    # archive_books_count = models.IntegerField(default=0, verbose_name='Количество купленных книг из архива')

    def __repr__(self):
        return 'Статистика'

    def __str__(self):
        return 'Статистика'

    def get_absolute_url(self):
        return reverse('get_stats')

    class Meta:
        db_table = 'statistic'
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
