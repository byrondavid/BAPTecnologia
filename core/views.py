from rest_framework.viewsets import ModelViewSet

from core import serializers, models


# Create your views here.


class CategoriaViewSet(ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer


class ProductoViewSet(ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer


class ServicioViewSet(ModelViewSet):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.ServicioSerializer


class ClienteViewSet(ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer


class ServiciosClienteViewSet(ModelViewSet):
    queryset = models.ServiciosCliente.objects.all()
    serializer_class = serializers.ServiciosClienteSerializer

class FotosServicioViewSet(ModelViewSet):
    queryset = models.FotoServicio.objects.all()
    serializer_class = serializers.FotoServicioSerializer
