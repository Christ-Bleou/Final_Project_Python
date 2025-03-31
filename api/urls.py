from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import OeuvreViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'oeuvres', OeuvreViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
