from django.db import models

from book_archive.models import BookArchive
from config.models import User
from book.models import Book
from subscribe.models import SubPrice


class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    type = models.CharField(max_length=128, verbose_name='Тип')
    top_up = models.IntegerField(blank=True, null=True, verbose_name='Сумма пополнения')
    payment_id = models.CharField(max_length=128, verbose_name='Способ оплаты', blank=True, null=True)
    payload = models.CharField(max_length=128, verbose_name='Payload', blank=True)

    class Meta:
        db_table = 'operation'
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f'{self.id}'


class PaymentStatus(models.Model):
    name = models.CharField(max_length=64)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'payment_status'
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплаты'
