from django.contrib import admin
from django.urls import path, include
import login.views

urlpatterns = [
    path('login/', login.views.login, name='login'),
    path('accounts/', include('allauth.urls')),  
    path('logout', login.views.logout_view, name="logout"),
]