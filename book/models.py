from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import signals

from book.tasks import send_tg_notifications
from config.models import User, Language


class Book(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала сбора')
    end_date = models.DateField(verbose_name='Дата конца сбора')
    goal_sum = models.IntegerField(verbose_name='Необходимая сумма')
    collected_sum = models.IntegerField(default=0, verbose_name='Собранная сумма')
    link = models.CharField(max_length=256, verbose_name='Ссылка на книгу', null=True, blank=True)
    is_done = models.BooleanField(default=False, verbose_name='Собрано ли')
    price_after_done = models.IntegerField(verbose_name='Цена после сбора')
    price_for_sub = models.IntegerField(verbose_name='Цена для подписчика')
    price_common = models.IntegerField(verbose_name='Цена для не подписчика')
    user = models.ManyToManyField(User, verbose_name='Заплатившие пользователи', blank=True)
    is_available = models.BooleanField('Доступна ли для скачивания', default=False, blank=True)
    is_notification_sent = models.BooleanField('Отправлено ли уведомление', default=False, blank=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        ids = [int(a.id) for a in list(Book.objects.all())]
        if ids:
            self.pk = max(ids) + 1
        else:
            self.pk = 1
        super().save(*args, **kwargs)

    def clean_fields(self, exclude=None):
        if self.link and 'http' not in self.link:
            raise ValidationError({'link': 'Некорректная ссылка. Оставьте поле пустым или введите корректную'})


def book_post_save(sender, instance, signal, *args, **kwargs):
    if instance.is_available and instance.is_done:
        user_ids = [u.telegram_id for u in instance.user.all()]
        print(instance.name, user_ids)
        instance.is_notification_sent = True
        send_tg_notifications.delay(user_ids, f'Книга {instance.name} доступна для скачивания!')


signals.post_save.connect(book_post_save, sender=Book)
