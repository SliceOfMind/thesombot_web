# Generated by Django 4.1.1 on 2022-10-12 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('value', models.IntegerField(verbose_name='Цена')),
                ('duration', models.IntegerField(verbose_name='Месяцы')),
            ],
            options={
                'verbose_name': 'Цена на подписку',
                'verbose_name_plural': 'Цены на подписки',
                'db_table': 'sub_price',
            },
        ),
        migrations.CreateModel(
            name='SubscribeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('value', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'subscribe_status',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата конца')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна ли')),
                ('sub_price_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscribe.subprice', verbose_name='Подписка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'db_table': 'subscribe',
            },
        ),
    ]