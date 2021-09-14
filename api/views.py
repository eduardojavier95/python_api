from rest_framework import viewsets

from .serializers import *


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PreOrdenViewSet(viewsets.ModelViewSet):
    queryset = PreOrden.objects.all()
    serializer_class = PreOrdenSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [permissions.IsAuthenticated]


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    # permission_classes = [permissions.IsAuthenticated]
