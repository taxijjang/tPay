from rest_framework.viewsets import ModelViewSet
from ..serializers.product_serializers import ProductSerializer,ProductOptionSerializer, TagSerializer

from ..models import Product, ProductOption, Tag

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer