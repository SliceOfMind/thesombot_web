# Generated by Django 4.1.1 on 2022-10-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
    ]
