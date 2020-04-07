from rest_framework import routers


from .viewsets import PesajeViewSet, PesajeExternoViewSet, UserViewSet, ProductoViewSet
from .viewsets import Pesaje_Today_ViewSet, PesajeExterno_Today_ViewSet

from django.urls import path
from django.conf.urls import include



#definira rutas get, post, put, delete
router = routers.SimpleRouter()
router.register('pesaje', PesajeViewSet)
router.register('pesaje_today',Pesaje_Today_ViewSet)
router.register('pesaje_externo', PesajeExternoViewSet)
router.register('pesaje_externo_today', PesajeExterno_Today_ViewSet)
router.register('producto', ProductoViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('',include(router.urls))
]
