from django.shortcuts import render, get_object_or_404
# Explicitation
from ecommerce.models import Oeuvre 

def catalogue(request):
    oeuvres = Oeuvre.objects.filter(disponible=True)
    return render(request, 'ecommerce/catalogue.html', {'oeuvres': oeuvres})

def detail_oeuvre(request, id):
    oeuvre = get_object_or_404(Oeuvre, id=id)
    return render(request, 'ecommerce/detail_oeuvre.html', {'oeuvre': oeuvre})

