from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userhandler.urls')),
    path('app/', include('app.urls'))
]

# Provisional method of leading user files, as for non-Heroku-actual-production level sites, it should be configured to save these files in like AWS
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
