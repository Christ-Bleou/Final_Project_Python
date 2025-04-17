from django import forms
from django.contrib.auth.forms import UserCreationForm
from ecommerce.models import Oeuvre, Commentaire, Utilisateur

class OeuvreForm(forms.ModelForm):
    class Meta:
        model = Oeuvre
        fields = ['titre', 'description', 'prix_location', 'image', 'disponible']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Écrire un commentaire...'})
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']