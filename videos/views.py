from django.http import JsonResponse
from .models import Video

def api_videos(request):
    videos = Video.objects.all().values('id', 'titre', 'publie', 'video_url')
    return JsonResponse(list(videos), safe=False)
