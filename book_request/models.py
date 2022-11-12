from django.db import models

from book_archive.models import Genre
from config.models import User


class BookRequest(models.Model):
    title = models.CharField('Наименование', max_length=128)
    author = models.CharField('Автор', max_length=128, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанры', null=True, blank=True)
    year = models.PositiveIntegerField('Год', default=0)
    created_at = models.DateTimeField('Дата запроса', auto_now_add=True)
    user = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.CASCADE, verbose_name='Кто добавил',
    )
    is_approved = models.BooleanField('Одобрено ли', null=True, blank=True)

    class Meta:
        db_table = 'book_request'
        verbose_name = 'Запрос книги'
        verbose_name_plural = 'Запросы книг'

    def __str__(self):
        return f'{self.title}'
