from django.db import models

# Create your models here.

class Pesaje(models.Model):
    peso = models.DecimalField(max_digits=8, decimal_places=3)
    placa = models.CharField(max_length=12)
    fecha_ingreso = models.DateField(auto_now_add=True)
