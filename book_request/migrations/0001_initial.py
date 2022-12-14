# Generated by Django 4.1.1 on 2022-10-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Наименование')),
                ('author', models.CharField(blank=True, max_length=128, null=True, verbose_name='Автор')),
                ('year', models.PositiveIntegerField(default=0, verbose_name='Год')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')),
                ('is_approved', models.BooleanField(blank=True, null=True, verbose_name='Одобрено ли')),
            ],
            options={
                'verbose_name': 'Запрос книги',
                'verbose_name_plural': 'Запросы книг',
                'db_table': 'book_request',
            },
        ),
    ]
