from django.contrib import admin
from django.urls import path
from videos.views import api_videos, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/videos/', api_videos),
    path('', home),
]
