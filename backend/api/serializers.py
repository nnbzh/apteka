from rest_framework import serializers
from api.models import SubCategory, Type, Category, \
    Pharmacy, Description, Manufacturer, Product


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    type_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Category
        fields = ('id', 'name')