from django.db import models
from django.urls import reverse

from common.models import SingletonModel


class Language(models.Model):
    language_code = models.CharField('Код языка', max_length=2, default='en', blank=True)
    name = models.CharField(max_length=64, verbose_name='Название языка')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'language'
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Referral(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    code = models.CharField(max_length=128, verbose_name='Код', unique=True)
    link = models.CharField(max_length=256, verbose_name='Ссылка', blank=True, null=True)
    register_count = models.IntegerField(default=0, verbose_name='Кол-во регистраций')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'referral'
        verbose_name = 'Реферальный код'
        verbose_name_plural = 'Реферальные коды'


class User(models.Model):
    telegram_id = models.BigIntegerField(verbose_name='ID пользователя в Telegram')
    username = models.CharField(max_length=128, verbose_name='Имя пользователя')
    mention = models.CharField(max_length=128, verbose_name='Обращение')
    balance = models.IntegerField(default=0, verbose_name='Баланс')
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE, verbose_name='Реферал', blank=True, null=True)
    is_block = models.BooleanField(default=False, verbose_name='Заблокировал ли бота')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык', blank=True)
    show_progress = models.BooleanField(default=False, verbose_name='Показывать ли прогресс сбора')
    deposit = models.IntegerField(default=0, verbose_name='Депозит')
    subscribe_time = models.IntegerField(default=0, verbose_name='Месяцы подписки')
    payment_id = models.CharField(max_length=128, verbose_name='Сохраненный способ оплаты', blank=True, null=True)
    is_auto_pay = models.BooleanField(default=True, verbose_name='Автоплатеж')
    subscribe_status = models.ForeignKey('subscribe.SubscribeStatus', on_delete=models.CASCADE, default=1)
    not_end_payment = models.BooleanField(verbose_name='Не закончил оплату', default=False)

    def __repr__(self):
        return str(self.telegram_id)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('get_user', kwargs={'user_id': int(self.pk)})

    class Meta:
        db_table = 'bot_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи бота'


class Question(models.Model):
    text = models.TextField(verbose_name='Текст')
    answer = models.TextField(default=None, null=True, verbose_name='Ответ')
    is_answered = models.BooleanField(default=False, verbose_name='Отвечен ли')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='От пользователя')
    date = models.DateTimeField(verbose_name='Дата вопроса', auto_created=True, auto_now=True)

    def __repr__(self):
        return f'Вопрос №{self.pk}'

    def __str__(self):
        return f'Вопрос №{self.pk}'

    class Meta:
        db_table = 'question'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Settings(SingletonModel):
    name = models.CharField(max_length=64)
    question_symbols_limit = models.IntegerField(default=300, verbose_name='Лимит символов в вопросе (0 для отключения)')
    top_up_limit = models.IntegerField(default=10000, verbose_name='Лимит пополнения баланса')
    book_title_limit = models.IntegerField(default=128, verbose_name='Лимит для названия предложенной книги')
    promo_code_limit = models.IntegerField(default=64, verbose_name='Лимит длины промокода')
    author_limit = models.IntegerField(default=256, verbose_name='Лимит для автора')

    def __repr__(self):
        return 'Настройки'

    def __str__(self):
        return 'Настройки'

    class Meta:
        db_table = 'settings'
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'
