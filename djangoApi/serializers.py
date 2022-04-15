
from rest_framework import serializers
from djangoApi.models import Product, Operation


# PRODUCT MODEL SERIALIZER
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'measurement_unit']

    # Validating Measurement Field
    def validate_measurement_unit(self, data):
        if data not in ['Kg', 'Liters', 'Units']:
            raise serializers.ValidationError('Choose from the choices (Kg,Liters,Units)')
        return data


# OPERATION MODEL SERIALIZER
class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['date', 'id', 'direction', 'amount']

    # Validating Direction Field
    def validate_direction(self, data):
        if data not in ['IN', 'OUT']:
            raise serializers.ValidationError('Choose from the choices (IN,OUT)')
        return data
