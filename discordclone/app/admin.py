from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Server)
admin.site.register(ServerMessage)
admin.site.register(Message)
admin.site.register(Role)
admin.site.register(TextChannel)
admin.site.register(VoiceChannel)
