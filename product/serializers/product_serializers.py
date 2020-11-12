from ..models import Product, Tag, ProductOption
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TagSerializer(WritableNestedModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Tag
        fields = ('pk', 'name',)


class ProductOptionSerializer(WritableNestedModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = ProductOption
        fields = ('pk', 'name', 'price',)


class ProductSerializer(WritableNestedModelSerializer):
    name = serializers.CharField()

    tag_set = TagSerializer(many=True, read_only=False)
    option_set = ProductOptionSerializer(many=True, read_only=False)

    class Meta:
        model = Product
        fields = ('pk', 'name', 'option_set', 'tag_set',)
