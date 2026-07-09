from django.urls import path
from .views import api_videos

urlpatterns = [
    path('api/videos/', api_videos),
]
