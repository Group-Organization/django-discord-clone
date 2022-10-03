from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('friends/', views.friends, name='friends'),
    # Url set to channel/pk/ as this is the structure from discord's online version kinda: discord.com/channels/<numbers>/<evenmorenumbers>
    path('server/<str:serverId>/<str:channelId>/', views.server, name="server"),
    path('add-friend/',
         views.addFriend, name='addFriend'),
    path('remove-friend/', views.removeFriend, name='removeFriend'),
    path('block-user/', views.blockUser, name='blockUser'),
    path('unblock-user/', views.unblockUser, name='unblockUser'),
    path('room/<str:room_name>', views.room, name="room"),
    path('test/', views.rooms, name='rooms')
]
