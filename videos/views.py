from django.http import JsonResponse
from django.shortcuts import render
from .models import Video

def api_videos(request):
    videos = Video.objects.all().values('id', 'titre', 'description', 'video_url', 'publie')
    return JsonResponse(list(videos), safe=False)

def home(request):
    videos = Video.objects.all().order_by('-publie')
    return render(request, 'videos/home.html', {'videos': videos})
