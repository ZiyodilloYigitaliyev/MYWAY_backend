from rest_framework import serializers
from .models import (
    ServiceAddres, TexServiceOrder, Gas, CarOil, TexServiceMessage
)

# ServiceAddres serializer
class ServiceAddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAddres
        fields = '__all__'

# TexServiceOrder serializer
class TexServiceOrderSerializer(serializers.ModelSerializer):
    locations = ServiceAddresSerializer()

    class Meta:
        model = TexServiceOrder
        fields = '__all__'
        read_only_fields = ['user']
# Gas serializer
class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = '__all__'
        read_only_fields = ['user']
# CarOil serializer
class CarOilSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOil
        fields = '__all__'
        read_only_fields = ['user']

# TexServiceMessage serializer
class TexServiceMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexServiceMessage
        fields = '__all__'
        read_only_fields = ['user']

