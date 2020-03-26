from rest_framework import serializers
from .models import Pesaje

class PesajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesaje
        fields = '__all__'