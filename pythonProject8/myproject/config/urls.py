from django.conf.global_settings import MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pygments.lexer import include

from myproject.config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('fly.urls', namespace="fly"))
] + static(settings.MEDIA.URL, document_root=settings,MEDIA_ROOT)