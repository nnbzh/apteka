from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'types', views.TypeViewSet, basename="Types")

urlpatterns = [
    path('', include(router.urls))
]