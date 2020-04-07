from django.contrib import admin

# Register your models here.

from .models import Pesaje, PesajeExterno

admin.site.register(Pesaje)

admin.site.register(PesajeExterno)