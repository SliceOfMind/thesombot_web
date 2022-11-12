from django.core.exceptions import ValidationError
from django.db import models

from config.models import User


class Genre(models.Model):
    title = models.CharField('Наименование', max_length=128, blank=True, null=True, default='1')
    number = models.CharField('Номер', max_length=8, default='1')

    def save(self, *args, **kwargs):
        ids = [int(a.id) for a in list(Genre.objects.all())]
        if ids:
            self.pk = max(ids) + 1
        else:
            self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'genre'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


class Author(models.Model):
    title = models.CharField('ФИО', max_length=256)

    def save(self, *args, **kwargs):
        ids = [int(a.id) for a in list(Author.objects.all())]
        if ids:
            self.pk = max(ids) + 1
        else:
            self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'author'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.title


class BookArchive(models.Model):
    title = models.CharField('Наименование', max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)
    year = models.IntegerField('Год', default=0, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    link = models.CharField('Ссылка на книгу', max_length=1024, null=True, blank=True)
    price = models.IntegerField('Цена', default=0)
    created_at = models.DateTimeField(auto_now=True)
    appeal = models.IntegerField(default=0, verbose_name='Кол-во обращений')

    class Meta:
        db_table = 'book_archive'
        verbose_name = 'Книга из архива'
        verbose_name_plural = 'Архив книг'

    def save(self, *args, **kwargs):
        ids = [int(a.id) for a in list(BookArchive.objects.all())]
        if ids:
            self.pk = max(ids) + 1
        else:
            self.pk = 1
        super().save(*args, **kwargs)

    def clean_fields(self, exclude=None):
        if self.link and 'http' not in self.link:
            raise ValidationError({'link': 'Некорректная ссылка. Оставьте поле пустым или введите корректную'})

    def __str__(self):
        return self.title


class PurchasedArchiveBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookArchive, on_delete=models.CASCADE)

    class Meta:
        db_table = 'purchased_archive_book'
