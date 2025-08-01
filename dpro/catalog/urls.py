from django.urls import path
from .views import home, contacts  # Явный импорт нужных функций

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]