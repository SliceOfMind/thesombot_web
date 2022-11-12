# Generated by Django 4.1.1 on 2022-10-12 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0001_initial'),
        ('book_request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='config.user', verbose_name='Кто добавил'),
        ),
    ]
