from xml.etree.ElementInclude import include

from django.contrib import admin
from dogs.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(('dogs.urls', 'dogs')))
]
