import django
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.db import models

from config.models import Language, User
from payment.models import PaymentStatus
from subscribe.models import SubscribeStatus


class Filter(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык', blank=True, null=True,
                                 default=0)
    subscribe_time_from = models.IntegerField(default=0, verbose_name='Месяцы подписки (От)')
    subscribe_time_to = models.IntegerField(default=0, verbose_name='Месяцы подписки (До)')
    deposit_from = models.IntegerField(default=0, verbose_name='Депозит (От)')
    deposit_to = models.IntegerField(default=0, verbose_name='Депозит (До)')
    balance_from = models.IntegerField(default=0, verbose_name='Баланс (От)')
    balance_to = models.IntegerField(default=0, verbose_name='Баланс (До)')
    subscribe_status = models.ForeignKey(SubscribeStatus, on_delete=models.CASCADE, verbose_name='Статус подписки',
                                         blank=True, null=True, default=None)
    not_end_payment = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE, verbose_name='Статус оплаты',
                                        default=3)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'filter'
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'


class Post(models.Model):
    title = models.TextField(
        validators=[MaxLengthValidator(limit_value=64, message='Ограничение заголовка - 64 символа')],
        verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    photo = models.FileField(upload_to='imgs/post/', verbose_name='Картинка/документ(pdf)', blank=True, null=True)
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    send_date = models.DateTimeField(verbose_name='Дата отправки', null=True, default=django.utils.timezone.now)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE, verbose_name='Фильтр', blank=True, null=True,
                               default=None)
    is_sent = models.BooleanField(verbose_name='Отправлен ли', default=False)
    link = models.CharField(max_length=128, verbose_name='Ссылка в кнопке', default='', blank=True, null=True)
    vote_options = models.TextField(verbose_name='Опрос(варианты с новой строки)', blank=True, null=True)

    def clean(self):
        if self.photo and (len(self.text) + len(self.title) >= 1024):
            raise ValidationError('Пост с картинкой или документом не должен быть длиннее 1024 символов')
        elif not self.photo and (len(self.text) + len(self.title) > 4096):
            raise ValidationError('Пост не должен быть длиннее 4096 символов')

    def clean_fields(self, exclude=None):
        if self.link and 'http' not in self.link:
            raise ValidationError({'link': 'Некорректная ссылка. Оставьте поле пустым или введите корректную'})

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostVote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', blank=True, null=True, default=None)
    title = models.CharField(max_length=128, verbose_name='Название опроса', blank=True, null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post_vote'
        verbose_name = 'Опрос в посте'
        verbose_name_plural = 'Опросы в посте'


class VoteChoice(models.Model):
    post_vote = models.ForeignKey(PostVote, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=128, verbose_name='Вариант опроса', blank=True, null=True, default=None)
    collected_votes = models.IntegerField(verbose_name='Проголосовало за этот вариант', blank=True, null=True,
                                          default=0)
    # must calc this field before page load

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = 'vote_choice'
        verbose_name = 'Вариант ответа в опросе'
        verbose_name_plural = 'Варианты ответов в вопросе'


class UserPoll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.ForeignKey(PostVote, on_delete=models.CASCADE)
    poll_id = models.CharField(max_length=128)
    choices = ArrayField(models.IntegerField(default=0))
    created_at = models.DateField(auto_now_add=True)
