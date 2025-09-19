# mailings/urls.py
from django.urls import path
from . import views

app_name = 'mailings'

urlpatterns = [
    path('', views.MailingListView.as_view(), name='mailing_list'),
    path('create/', views.MailingCreateView.as_view(), name='mailing_create'),
    path('detail/<int:pk>/', views.MailingDetailView.as_view(), name='mailing_detail'),
    path('update/<int:pk>/', views.MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', views.MailingDeleteView.as_view(), name='mailing_delete'),
    path('send/<int:pk>/', views.send_mailing_now, name='send_mailing'),
]