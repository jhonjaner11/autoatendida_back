from rest_framework import viewsets

from .models import Pesaje
from .serializer import PesajeSerializer

class PesajeViewSet(viewsets.ModelViewSet):
    queryset = Pesaje.objects.all()
    serializer_class = PesajeSerializer