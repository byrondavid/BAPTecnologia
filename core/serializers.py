from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from core.models import *


class FotoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoProducto
        fields = ALL_FIELDS


class FotoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoServicio
        fields = ALL_FIELDS


class FotoSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoSeguimiento
        fields = ALL_FIELDS


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ALL_FIELDS


class ProductoSerializer(serializers.ModelSerializer):
    fotos_producto = FotoProductoSerializer(
        many=True,
        source='fotoproducto_set'
    )

    categoria = CategoriaSerializer()

    class Meta:
        model = Producto
        fields = ALL_FIELDS


class ServicioSerializer(serializers.ModelSerializer):
    fotos_servicio = FotoServicioSerializer(
        many=True,
        source='fotoservicio_set'
    )

    class Meta:
        model = Servicio
        fields = ALL_FIELDS


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ALL_FIELDS


class SeguimientoSerializer(serializers.ModelSerializer):
    fotos_seguimiento = FotoSeguimientoSerializer(
        many=True,
        source='fotoseguimiento_set'
    )

    class Meta:
        model = Seguimiento
        fields = ALL_FIELDS


class ServiciosClienteSerializer(serializers.ModelSerializer):
    servicio = ServicioSerializer()
    cliente = ClienteSerializer()
    class Meta:
        model = ServiciosCliente
        fields = ALL_FIELDS
