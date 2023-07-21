from django.urls import path, include
from .views import UserViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
