from django.urls import path
from . import views

urlpatterns = [
    path('', views.service1, name='service1'),
]