from django.shortcuts import render

def index(request):
    return render(request, 'live/index.html')

# Create your views here.
