# Generated by Django 4.1.1 on 2022-10-21 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_archive', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookarchive',
            name='buy_count',
        ),
    ]