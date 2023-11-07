from rest_framework import serializers
from .models import Product
from .models import Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'