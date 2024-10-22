from rest_framework import serializers
from .models import *

# RestoreLicense serializer
class RestoreLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestoreLicense
        fields = '__all__'
        read_only_fields = ['user']

# Affidavit serializer
class AffidavitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affidavit
        fields = '__all__'
        read_only_fields = ['user']

# Department serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['user']


