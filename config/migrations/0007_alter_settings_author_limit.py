# Generated by Django 4.1.1 on 2022-11-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_remove_settings_book_request_title_limit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='author_limit',
            field=models.IntegerField(default=256, verbose_name='Лимит для автора'),
        ),
    ]
