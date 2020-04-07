from rest_framework import serializers
from .models import Pesaje, PesajeExterno, Producto
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PesajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesaje
        fields = '__all__'

class Pesaje_Today_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pesaje
        fields = '__all__'


class PesajeExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PesajeExterno
        fields = '__all__'

class PesajeExterno_Today_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PesajeExterno
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','password')
    extra_kwargs = {'password':{'write_only':True,'required':True}}

  def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      print(user)
      Token.objects.create(user=user)
      return user
