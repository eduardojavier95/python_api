from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet)
router.register('categoria', CategoriaViewSet)
router.register('producto', ProductoViewSet)
router.register('oferta', OfertaViewSet)
router.register('preorden', PreOrdenViewSet)
router.register('venta', VentaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
