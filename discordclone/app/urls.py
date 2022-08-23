from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('friends/', views.friends, name='friends'),
    path('friends/add-friend/<str:friendUsername>',
         views.addFriend, name='addFriend'),
    path('friends/removeFriend/<str:friendUsername>',
         views.removeFriend, name='removeFriend')
]
