from django.urls import path
from . import views

app_name = "fly"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.prod_detail, name="prod_detail"),
]
