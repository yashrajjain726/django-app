import requests
from rest_framework import serializers, request

from djangoApi.models import Product, Operation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'measurement_unit']

    def validate_measurement_unit(self, data):
        if data not in ['Kg', 'Liters', 'Units']:
            raise serializers.ValidationError('Choose from the choices (Kg,Liters,Units)')
        return data


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['date', 'id', 'direction', 'amount']

    def validate_direction(self, data):
        if data not in ['IN', 'OUT']:
            raise serializers.ValidationError('Choose from the choices (IN,OUT)')
        return data
