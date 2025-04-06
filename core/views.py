from django.shortcuts import render

def page_a_propos(request):
    return render(request, 'D:\\Final_Project_Python\\art_rental\\core\\templates\\core\\a_propos.html')

def page_confidentialite(request):
    return render(request, 'D:\\Final_Project_Python\\art_rental\\core\\templates\\core\\confidentialite.html')
