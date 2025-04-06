from django.contrib import admin
# Explicitation
from ecommerce.models import Oeuvre, Location, Utilisateur

@admin.register(Oeuvre)
class OeuvreAdmin(admin.ModelAdmin):
    list_display = ['titre', 'artiste', 'disponible', 'prix_location']
    list_filter = ['disponible']
    search_fields = ['titre', 'description']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['oeuvre', 'client', 'date_debut', 'date_fin', 'statut']
    list_filter = ['statut',]
    search_fields = ['client', 'oeuvre']
