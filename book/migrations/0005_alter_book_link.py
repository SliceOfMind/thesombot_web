# Generated by Django 4.1.1 on 2022-10-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ссылка на книгу'),
        ),
    ]