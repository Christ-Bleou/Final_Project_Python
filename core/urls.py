from django.urls import path
# Explicitation
from core import views

urlpatterns = [
    path('a_propos/', views.page_a_propos, name='a_propos'),
    path('confidentialite/', views.page_confidentialite, name='confidentialite'),
]
