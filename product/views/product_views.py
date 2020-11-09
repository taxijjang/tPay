from rest_framework.viewsets import ModelViewSet
from ..serializers.product_serializers import ProductSerializer

from ..models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
