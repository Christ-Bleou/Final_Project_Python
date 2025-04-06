from django.urls import path
# Explicitation
from blog import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('article/<int:id>/', views.detail_article, name='detail_article'),
]
