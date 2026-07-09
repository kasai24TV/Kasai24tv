from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste, name='liste'),  # Page d'accueil
    path('categorie/<str:cat>/', views.categorie, name='categorie'),  # Ex: /categorie/sport/
    path('article/<int:id>/', views.detail_article, name='detail'),  # Ex: /article/3/
    path('direct/', views.direct, name='direct'),  # Page du direct
]
