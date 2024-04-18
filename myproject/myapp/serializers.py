from rest_framework import serializers
from .models import ForeignKeyModel, MainModel

class ForeignKeyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignKeyModel
        fields = '__all__'

class MainModelSerializer(serializers.ModelSerializer):
    foreign_key_field = serializers.PrimaryKeyRelatedField(queryset=ForeignKeyModel.objects.all())

    class Meta:
        model = MainModel
        fields = ['name', 'foreign_key_field']
