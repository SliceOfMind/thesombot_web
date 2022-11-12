from django.db import models

from config.models import User


class SubPrice(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    value = models.IntegerField(verbose_name='Цена')
    duration = models.IntegerField(verbose_name='Месяцы')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub_price'
        verbose_name = 'Цена на подписку'
        verbose_name_plural = 'Цены на подписки'


class Subscribe(models.Model):
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата конца')
    is_active = models.BooleanField(default=True, verbose_name='Активна ли')
    sub_price = models.ForeignKey(SubPrice, on_delete=models.CASCADE, verbose_name='Подписка')
    user = models.ForeignKey('config.User', on_delete=models.CASCADE, verbose_name='Пользователь')

    def __repr__(self):
        return f'Подписка'

    def __str__(self):
        return f''

    class Meta:
        db_table = 'subscribe'
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class SubscribeStatus(models.Model):
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subscribe_status'
