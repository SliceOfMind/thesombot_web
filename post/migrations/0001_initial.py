# Generated by Django 4.1.1 on 2022-10-12 15:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscribe', '0001_initial'),
        ('payment', '0001_initial'),
        ('config', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('subscribe_time_from', models.IntegerField(default=0, verbose_name='Месяцы подписки (От)')),
                ('subscribe_time_to', models.IntegerField(default=0, verbose_name='Месяцы подписки (До)')),
                ('deposit_from', models.IntegerField(default=0, verbose_name='Депозит (От)')),
                ('deposit_to', models.IntegerField(default=0, verbose_name='Депозит (До)')),
                ('balance_from', models.IntegerField(default=0, verbose_name='Баланс (От)')),
                ('balance_to', models.IntegerField(default=0, verbose_name='Баланс (До)')),
                ('language', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='config.language', verbose_name='Язык')),
                ('not_end_payment', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='payment.paymentstatus', verbose_name='Статус оплаты')),
                ('subscribe_status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='subscribe.subscribestatus', verbose_name='Статус подписки')),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтры',
                'db_table': 'filter',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(validators=[django.core.validators.MaxLengthValidator(limit_value=64, message='Ограничение заголовка - 64 символа')], verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('photo', models.FileField(blank=True, null=True, upload_to='imgs/post/', verbose_name='Картинка/документ(pdf)')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Дата отправки')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Отправлен ли')),
                ('link', models.CharField(blank=True, default='', max_length=128, verbose_name='Ссылка в кнопке')),
                ('vote_options', models.TextField(blank=True, null=True, verbose_name='Опрос(варианты с новой строки)')),
                ('filter', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.filter', verbose_name='Фильтр')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='PostVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default=None, null=True, verbose_name='Название')),
                ('post', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Пост - голосование',
                'verbose_name_plural': 'Посты - голосования',
                'db_table': 'post_vote',
            },
        ),
        migrations.CreateModel(
            name='PostVoteOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default=None, null=True, verbose_name='Вариант опроса')),
                ('collected_votes', models.IntegerField(blank=True, default=0, null=True, verbose_name='Проголосовало за этот вариант')),
                ('post_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.postvote')),
            ],
            options={
                'verbose_name': 'Пост - голосование вариант',
                'verbose_name_plural': 'Посты - голосования варианты',
                'db_table': 'post_vote_options',
            },
        ),
    ]
