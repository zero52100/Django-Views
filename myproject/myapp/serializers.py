from rest_framework import serializers
from .models import ForeignKeyModel, MainModel

class ForeignKeyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignKeyModel
        fields = '__all__'

class MainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = '__all__'
