import random
import string

from django.db import models
from config.models import User
from subscribe.models import SubPrice
from thesombot_web.settings import PROMO_CODE_LENGTH


class PromoCode(models.Model):
    ONETIME, MANYTIME = 'O', 'M'
    ONEUSER, MULTIUSER = 'O', 'M'
    TIME_MODES = (
        (ONETIME, 'Одноразовый'),
        (MANYTIME, 'Многоразовый'),
    )
    USER_MODES = (
        (ONEUSER, 'Однопользовательский'),
        (MULTIUSER, 'Многопользовательский'),
    )
    time_mode = models.CharField('Одно/многоразовый', max_length=1, choices=TIME_MODES, default=ONETIME)
    user_mode = models.CharField('Одно/многопользовательский', max_length=1, choices=USER_MODES, default=ONEUSER)
    promo_code = models.CharField(max_length=64, verbose_name='Промокод', unique=True, blank=True, default='')
    discount = models.IntegerField(verbose_name='Скидка')
    sub_price_id = models.ManyToManyField(SubPrice, verbose_name='На какие подписки')
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    def __repr__(self):
        return self.promo_code

    def __str__(self):
        return self.promo_code

    def save(self, *args, **kwargs):
        if not self.promo_code:
            letters = string.ascii_uppercase
            rand_string = ''.join(random.choice(letters) for i in range(int(PROMO_CODE_LENGTH)))
            self.promo_code = rand_string
        ids = [int(a.id) for a in list(PromoCode.objects.all())]
        if ids:
            self.pk = max(ids) + 1
        else:
            self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'promo_code'
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'


class PromoCodeUser(models.Model):
    ACTIVE, INACTIVE = '1', '0'
    ACTIVITY = (
        (ACTIVE, 'Активен'),
        (INACTIVE, 'Не активен'),
    )
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.CharField('Активен', max_length=1, choices=ACTIVITY, default=ACTIVE)

    def __str__(self):
        return f'{self.user.username}: {self.promo_code.promo_code}'

    class Meta:
        db_table = 'promo_code_user'
        verbose_name = 'Пользователь промокода'
        verbose_name_plural = 'Пользователи промокода'



