from django.shortcuts import render, get_object_or_404
from .models import Actualite

def liste(request):
    actualites = Actualite.objects.all()
    return render(request, 'television/liste.html', {'actualites': actualites})

def categorie(request, cat):
    actualites = Actualite.objects.filter(resume__icontains=cat)
    return render(request, 'television/liste.html', {'actualites': actualites})

def detail_article(request, id):
    act = get_object_or_404(Actualite, id=id)
    return render(request, 'television/detail.html', {'act': act})

def direct(request):
    return render(request, 'television/direct.html')
