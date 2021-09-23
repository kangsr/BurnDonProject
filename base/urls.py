from django.urls import path, include
from . import views
import login.urls, fire.urls, bucket_list.urls

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', include(login.urls)),
    path('fire/', include(fire.urls)),
    path('bucket_list/', include(bucket_list.urls)),
]