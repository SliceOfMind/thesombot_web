# Generated by Django 4.1.1 on 2022-10-23 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promo_code', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocode',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='promocode',
            name='is_used',
        ),
    ]
