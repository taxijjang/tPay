

from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from .views.product_views import ProductViewSet



router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
]


