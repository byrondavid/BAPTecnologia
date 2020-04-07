from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from core.models import Foto, Categoria, Producto, Servicio, Cliente, \
    Seguimiento, ServiciosCliente


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ALL_FIELDS


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ALL_FIELDS


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ALL_FIELDS


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ALL_FIELDS


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ALL_FIELDS


class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = ALL_FIELDS


class ServiciosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosCliente
        fields = ALL_FIELDS
