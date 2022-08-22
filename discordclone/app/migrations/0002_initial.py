# Generated by Django 3.2.7 on 2022-08-22 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textchannel',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='ChannelParticipants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='textchannel',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.server'),
        ),
        migrations.AddField(
            model_name='server',
            name='messages',
            field=models.ManyToManyField(blank=True, related_name='messages', to='app.Message'),
        ),
        migrations.AddField(
            model_name='server',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='server',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='server',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='roles', to='app.Role'),
        ),
        migrations.AddField(
            model_name='server',
            name='text_channels',
            field=models.ManyToManyField(blank=True, related_name='text_channels', to='app.TextChannel'),
        ),
        migrations.AddField(
            model_name='role',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, to='app.server'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='servermessage',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.textchannel'),
        ),
        migrations.AddField(
            model_name='servermessage',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.server'),
        ),
        migrations.AddField(
            model_name='server',
            name='voice_channels',
            field=models.ManyToManyField(blank=True, related_name='voice_channels', to='app.VoiceChannel'),
        ),
    ]
