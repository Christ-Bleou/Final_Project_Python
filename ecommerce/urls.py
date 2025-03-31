from django.urls import path
# Explicitation
from ecommerce import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('oeuvre/<int:id>/', views.detail_oeuvre, name='detail_oeuvre'),
]
