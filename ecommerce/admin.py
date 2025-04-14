from django.contrib import admin
# Explicitation
from ecommerce.models import Oeuvre, Location, Utilisateur

from django.utils.html import format_html
from django.templatetags.static import static

# from django.contrib.admin.sites import AlreadyRegistered

@admin.register(Oeuvre)
class OeuvreAdmin(admin.ModelAdmin):
    list_display = ['titre', 'artiste', 'disponible', 'prix_location', 'affiche_image']
    list_filter = ['disponible']
    search_fields = ['titre', 'description']

    def affiche_image(self, obj):
        if obj.image:
            url = static('img/' + obj.image)
            return format_html('<img src="{}" width="255" height="auto" />', url)
        return "Aucune image"
    affiche_image.short_description = "Aperçu"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['oeuvre', 'client', 'date_debut', 'date_fin', 'statut']
    list_filter = ['statut',]
    search_fields = ['client', 'oeuvre']
