# Generated by Django 4.1.1 on 2022-10-12 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='BookArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Наименование')),
                ('year', models.CharField(blank=True, max_length=256, null=True, verbose_name='Год')),
                ('link', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Ссылка на книгу')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('appeal', models.IntegerField(default=0, verbose_name='Кол-во обращений')),
                ('buy_count', models.IntegerField(default=0, verbose_name='Кол-во покупок')),
            ],
            options={
                'verbose_name': 'Книга из архива',
                'verbose_name_plural': 'Архив книг',
                'db_table': 'book_archive',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='PurchasedArchiveBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_archive.bookarchive')),
            ],
            options={
                'db_table': 'purchased_archive_book',
            },
        ),
    ]