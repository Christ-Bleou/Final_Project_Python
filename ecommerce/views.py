from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.conf import settings

# Explicitation
from ecommerce.models import Oeuvre, Location
from ecommerce.form import OeuvreForm

import os

def catalogue(request):
    oeuvres = Oeuvre.objects.filter(disponible=True)
    return render(request, 'ecommerce/catalogue.html', {'oeuvres': oeuvres})

def detail_oeuvre(request, id):
    oeuvre = get_object_or_404(Oeuvre, id=id)
    return render(request, 'ecommerce/detail_oeuvre.html', {'oeuvre': oeuvre})

def base(request):
    return render(request, 'ecommerce/base.html')

@login_required
def ajouter_oeuvre(request):
    template_path = os.path.join(settings.BASE_DIR, 'ecommerce/templates/ecommerce/ajouter_oeuvre.html')
    print(f"Vérification du chemin du template : {template_path} - Existe : {os.path.exists(template_path)}")
    # Optionnel: Vérifier que l'utilisateur est bien un artiste
    if request.user.role != 'artiste':
        return redirect('catalogue')
        
    if request.method == 'POST':
        form = OeuvreForm(request.POST, request.FILES)
        if form.is_valid():
            oeuvre = form.save(commit=False)
            oeuvre.artiste = request.user  # Associer l'œuvre à l'artiste connecté
            oeuvre.save()
            return redirect('catalogue')
    else:
        form = OeuvreForm()
    return render(request, 'ecommerce/ajouter_oeuvre.html', {'form': form})

def ajouter_oeuvre_2(request):
    return render(request, 'ecommerce/test.html')

# Vue pour afficher les locations de l'utilisateur connecté
@login_required
def mes_locations(request):
    # On utilise le related_name "locations" défini sur le modèle Location
    locations = request.user.locations.all()
    return render(request, 'ecommerce/mes_locations.html', {'locations': locations})

# Vue de connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('catalogue')
    else:
        form = AuthenticationForm()
    return render(request, 'ecommerce/login.html', {'form': form})

# Vue d'inscription
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connecte automatiquement l'utilisateur après inscription
            login(request, user)
            return redirect('catalogue')
    else:
        form = UserCreationForm()
    return render(request, 'ecommerce/register.html', {'form': form})

# Vue de déconnexion
def logout_view(request):
    logout(request)
    return redirect('base')