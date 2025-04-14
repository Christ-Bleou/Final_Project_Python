from django.urls import path
# Explicitation
from ecommerce import views

urlpatterns = [
    path('', views.base, name='base'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('oeuvre/<int:id>/', views.detail_oeuvre, name='detail_oeuvre'),
    path('oeuvre/<int:id>/louer/', views.louer_oeuvre, name='louer_oeuvre'),
    path('test/', views.ajouter_oeuvre_2, name='test'),
    path('ajouter/', views.ajouter_oeuvre, name='ajouter_oeuvre'),
    path('locations/', views.mes_locations, name='mes_locations'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
