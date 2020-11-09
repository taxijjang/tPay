from ..models import Product, Tag, ProductOption
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Tag
        fields = ('pk', 'name',)


class ProductOptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = ProductOption
        fields = ('pk', 'name', 'price',)

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    tag_set = TagSerializer(many=True)

    option_set = ProductOptionSerializer(many=True)

    class Meta:
        model = Product
        fields = ('pk','name','option_set', 'tag_set',)