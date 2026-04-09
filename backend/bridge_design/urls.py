from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationDataViewSet, BridgeDesignViewSet

router = DefaultRouter()
router.register(r'locations', LocationDataViewSet)
router.register(r'designs', BridgeDesignViewSet)

urlpatterns = [
    path('', include(router.urls)),
]