# Generated by Django 3.2.15 on 2022-08-18 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=256)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('created', models.DateTimeField(auto_now=True)),
                ('messages', models.ManyToManyField(blank=True, related_name='messages', to='app.Message')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL)),
                ('roles', models.ManyToManyField(blank=True, related_name='roles', to='app.Role')),
            ],
        ),
        migrations.CreateModel(
            name='TextChannel',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('participants', models.ManyToManyField(blank=True, related_name='ChannelParticipants', to=settings.AUTH_USER_MODEL)),
                ('server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.server')),
            ],
        ),
        migrations.CreateModel(
            name='VoiceChannel',
            fields=[
                ('textchannel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.textchannel')),
            ],
            bases=('app.textchannel',),
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
        migrations.CreateModel(
            name='ServerMessage',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.message')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.textchannel')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.server')),
            ],
            bases=('app.message',),
        ),
        migrations.AddField(
            model_name='server',
            name='voice_channels',
            field=models.ManyToManyField(blank=True, related_name='voice_channels', to='app.VoiceChannel'),
        ),
    ]