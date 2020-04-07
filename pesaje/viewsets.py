
from .models import Pesaje, PesajeExterno, Producto
from .serializer import PesajeSerializer, PesajeExternoSerializer, UserSerializer, ProductoSerializer

from .serializer import Pesaje_Today_Serializer, PesajeExterno_Today_Serializer
import datetime
from datetime import timedelta, date


from django.shortcuts import render
from rest_framework import viewsets, status

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


class PesajeViewSet(viewsets.ModelViewSet):
    queryset = Pesaje.objects.all()
    serializer_class = PesajeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,) #IsAuthenticated
    #Pesaje.objects.filter(fecha_ingreso=datetime.datetime.now())
    # 


class Pesaje_Today_ViewSet(viewsets.ModelViewSet):

    new =  date.today() + timedelta(days=1)        
    queryset =  Pesaje.objects.filter(fecha_ingreso__range=(date.today(),new))   
    serializer_class = Pesaje_Today_Serializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,) #IsAuthenticated

    
   
    #Pesaje.objects.filter(fecha_ingreso=datetime.datetime.now())    
    #Pesaje.objects.filter(fecha_ingreso__range=('2020-04-02','2020-04-03')) 

class PesajeExternoViewSet(viewsets.ModelViewSet):
    queryset = PesajeExterno.objects.all()
    serializer_class = PesajeExternoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class PesajeExterno_Today_ViewSet(viewsets.ModelViewSet):

    new =  date.today() + timedelta(days=1)        
    queryset =  PesajeExterno.objects.filter(fecha_ingreso__range=(date.today(),new))   
    serializer_class = PesajeExterno_Today_Serializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,) #IsAuthenticated


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

