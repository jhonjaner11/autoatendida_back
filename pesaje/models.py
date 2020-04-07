from django.db import models

# Create your models here.

class Pesaje(models.Model):

    peso_neto = models.DecimalField(max_digits=8, decimal_places=3,null=True)
    peso_salida = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    peso_ingreso = models.DecimalField(max_digits=8, decimal_places=3)

    placa = models.CharField(max_length=12)

    fecha_ingreso = models.DateTimeField(auto_now_add=True )
    fecha_salida = models.DateTimeField(null=True)

class PesajeExterno(models.Model):
    peso_neto = models.DecimalField(max_digits=8, decimal_places=3,null=True)
    peso_salida = models.DecimalField(max_digits=8, decimal_places=3,null=True)
    peso_ingreso = models.DecimalField(max_digits=8, decimal_places=3)

    placa = models.CharField(max_length=12)

    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True)

class Producto(models.Model):
    codigo = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=12)
    cantidad = models.DecimalField(max_digits=8, decimal_places=3, null=True )
   
