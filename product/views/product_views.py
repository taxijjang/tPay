from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..serializers.product_serializers import ProductSerializer

from ..models import Product

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().prefetch_related('tag_set').prefetch_related('option_set')
        serializer = self.get_serializer(qs, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        qs = self.get_queryset().prefetch_related('tag_set').prefetch_related('option_set')
        instance = qs.filter(pk=pk)[0]
        serializer = self.get_serializer(instance=instance)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
