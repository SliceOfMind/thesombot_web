# Generated by Django 4.1.1 on 2022-10-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_archive', '0005_rename_book_id_purchasedarchivebook_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='number',
            field=models.CharField(default='1', max_length=8, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='bookarchive',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Наименование'),
        ),
    ]