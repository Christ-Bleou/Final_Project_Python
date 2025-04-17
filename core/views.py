from django.shortcuts import render

def page_a_propos(request):
    return render(request, 'core/a_propos.html')

def page_confidentialite(request):
    return render(request, 'core/confidentialite.html')
