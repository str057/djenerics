from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import UserRegisterView, UserLoginView, logout_view, UserProfileView
from mailings.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('clients/', include('clients.urls', namespace='clients')),
    path('messages/', include('messages_app.urls', namespace='messages_app')),
    path('mailings/', include('mailings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)