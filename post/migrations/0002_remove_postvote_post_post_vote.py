# Generated by Django 4.1.1 on 2022-10-13 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postvote',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.postvote', verbose_name='Голосование к посту'),
        ),
    ]
