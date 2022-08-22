from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('friends/', views.friends, name='friends'),
    # Url set to channel/pk/ as this is the structure from discord's online version kinda: discord.com/channels/<numbers>/<evenmorenumbers>
    path('channel/<str:pk>/', views.server, name="server"),
]
