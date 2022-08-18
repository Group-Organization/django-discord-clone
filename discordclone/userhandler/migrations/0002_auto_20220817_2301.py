# Generated by Django 3.2.15 on 2022-08-17 23:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userhandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 17, 23, 1, 44, 977123, tzinfo=utc)),
            preserve_default=False,
        ),
    ]