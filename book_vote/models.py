from django.db import models

from config.models import User


class VoteBook(models.Model):
    title = models.CharField('Наименование', max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')
    user = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.CASCADE, verbose_name='Кто добавил',
    )
    is_visible = models.BooleanField('Доступна ли для голосования', default=False)
    vote_goal = models.IntegerField('Необходимое кол-во голосов', blank=100, default=100)
    fund_interval = models.IntegerField('Время на сбор(в днях)', default=100)
    is_fund_sent = models.BooleanField('Ушла на франдрайз', default=False)
    # fields from book model

    description = models.TextField(verbose_name='Описание', default='Описание книги')
    fund_need = models.IntegerField('Необходимая сумма', default=1000)
    link = models.CharField(max_length=256, verbose_name='Ссылка на книгу', blank=True)
    price_after_done = models.IntegerField(verbose_name='Цена после сбора', default=0)
    price_for_sub = models.IntegerField(verbose_name='Цена для подписчика', default=0)
    price_common = models.IntegerField(verbose_name='Цена для не подписчика', default=0)

    class Meta:
        db_table = 'vote_book'
        verbose_name = 'Книга на голосование'
        verbose_name_plural = 'Книги на голосование'

    def __str__(self):
        return self.title


class UserBookVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Чей голос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')
    book = models.ForeignKey(
        VoteBook, on_delete=models.CASCADE,
        verbose_name='Книга за которую проголосовал',
    )

    class Meta:
        db_table = 'user_book_vote'
        verbose_name = 'Голос за книгу'
        verbose_name_plural = 'Голоса за книгу'

    def __str__(self):
        return f'{self.user.username}: {self.book.title}'
