# Generated by Django 4.1.1 on 2022-10-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
    ]
