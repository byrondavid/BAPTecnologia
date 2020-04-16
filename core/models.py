import os
from uuid import uuid4

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.deconstruct import deconstructible

# Create your models here.
from BAPTecnologia.settings import MEDIA_URL


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        print('PATH: ', self.path)
        return os.path.join(MEDIA_URL, filename)


path_and_rename = PathAndRename("/fotos")


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    ver_en_web = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=7)
    descuento = models.PositiveSmallIntegerField(null=True)
    ver_descuento = models.BooleanField(default=True)
    ver_en_web = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "" + self.nombre + " | " + self.categoria.nombre


class FotoProducto(models.Model):
    titulo = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ver_en_web = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, null=True, upload_to=path_and_rename)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " | PRODUCTO: " + self.producto.nombre


class Servicio(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=7)
    descuento = models.PositiveSmallIntegerField(null=True)
    ver_descuento = models.BooleanField(default=True)
    ver_en_web = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class FotoServicio(models.Model):
    titulo = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ver_en_web = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, null=True, upload_to=path_and_rename)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " | SERVICIO: " + self.servicio.titulo


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

    servicios = models.ManyToManyField(Servicio, through='ServiciosCliente')


class ServiciosCliente(models.Model):
    porcentaje_total = models.PositiveSmallIntegerField(default=0)

    observaciones = models.TextField(null=True)
    estado = models.CharField(max_length=30)

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Seguimiento(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(null=True)
    porcentaje = models.PositiveSmallIntegerField(default=0)

    servicio_cliente = models.ForeignKey(ServiciosCliente,
                                         on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class FotoSeguimiento(models.Model):
    titulo = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ver_en_web = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, null=True, upload_to=path_and_rename)
    seguimiento = models.ForeignKey(Seguimiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " | Seguimiento: " + self.seguimiento.titulo
