from django import forms
from ecommerce.models import Oeuvre

class OeuvreForm(forms.ModelForm):
    class Meta:
        model = Oeuvre
        fields = ['titre', 'description', 'prix_location', 'image', 'disponible']
