from rest_framework import routers


from .viewsets import PesajeViewSet

#definira rutas get, post, put, delete
router = routers.SimpleRouter()
router.register('pesajes', PesajeViewSet)

urlpatterns = router.urls