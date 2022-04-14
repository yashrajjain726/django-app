import requests
from rest_framework import serializers, request

from djangoApi.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product




class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    measurement_unit = serializers.CharField()

    def create(self, validate_data):
        return Product.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.measurement_unit = validated_data.get('measurement_unit', instance.measurement_unit)
        instance.save()
        return instance
