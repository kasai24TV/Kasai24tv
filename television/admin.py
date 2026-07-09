from django.contrib import admin
from .models import Actualite

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_pub', 'en_direct')
    list_filter = ('en_direct', 'date_pub')
    search_fields = ('titre', 'resume')
    list_editable = ('en_direct',)
