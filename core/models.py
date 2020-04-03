import os
from uuid import uuid4

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.deconstruct import deconstructible


# Create your models here.

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


path_and_rename = PathAndRename("/fotos")


class Foto(models.Model):
    foto = models.ImageField(blank=True, null=True, upload_to=path_and_rename)
    fecha_registro = models.DateTimeField(auto_now_add=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=7)
    descuento = models.PositiveSmallIntegerField(null=True)
    ver_descuento = models.BooleanField(default=True)
    ver_en_web = models.BooleanField(default=True)
    fotos = models.ManyToManyField(Foto)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Servicio(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=7)


class Cliente(models.Model):
    identificacion = models.CharField(max_length=30)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True)
    correo = models.EmailField(null=True)
    telefono = models.CharField(max_length=30)
    direccion = models.TextField(null=True)

    fotos = models.ManyToManyField(Foto)
    servicios = models.ManyToManyField(Servicio, through='ServiciosCliente')


class Seguimiento(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(null=True)
    porcentaje = models.PositiveSmallIntegerField(default=0)

    fotos = models.ManyToManyField(Foto)


class ServiciosCliente(models.Model):
    porcentaje_total = models.PositiveSmallIntegerField(default=0)

    equipo = JSONField(null=True)

    observaciones = models.TextField(null=True)
    estado = models.CharField(max_length=30)

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    seguimientos = models.ManyToManyField(Seguimiento)
