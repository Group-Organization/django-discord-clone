# Generated by Django 3.2.15 on 2022-08-19 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhandler', '0004_auto_20220819_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]
