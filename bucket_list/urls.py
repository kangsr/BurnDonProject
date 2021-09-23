from django.urls import path
from .views import *

urlpatterns = [
    path('new/', new, name="new"),
    path('list/', list, name="list"),
    path('edit/<str:id>', edit, name="edit"),
    path('delete/<str:id>', delete, name="delete"),
]