from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
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
        instance = self.get_queryset().filter(pk=pk).prefetch_related('tag_set').prefetch_related('option_set').first()
        serializer = self.get_serializer(instance)
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
