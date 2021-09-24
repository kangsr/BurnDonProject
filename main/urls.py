from django.urls import path
from .views import *

urlpatterns = [
    path('page2/', new, name="page2"),
    path('page5/', page5, name="page5"),
    path('page3', new2, name="page3"),
    path('page6', page6, name="page6"),
]