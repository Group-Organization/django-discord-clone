from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('friends/', views.friends, name='friends'),
    # Url set to channel/pk/ as this is the structure from discord's online version kinda: discord.com/channels/<numbers>/<evenmorenumbers>
    path('server/<str:serverId>/<str:channelId>/', views.server, name="server"),
    path('friends/add-friend/<str:friendUsername>/<str:friendTag',
         views.addFriend, name='addFriend'),
    path('friends/remove-friend/<str:friendUsername>/<str:friendTag>',
         views.removeFriend, name='removeFriend')
]
