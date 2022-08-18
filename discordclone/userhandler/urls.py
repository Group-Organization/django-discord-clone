from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.registerUser, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('profiles/', views.profiles, name='profiles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

