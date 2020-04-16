from django.contrib import admin

# Register your models here.
from django import forms

from core.forms import ServicioClienteForm
from core.models import *


class FotoProductoInline(admin.TabularInline):
    model = FotoProducto
    extra = 0
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'rows': 6, 'cols': 40})
        },
    }


class FotoServicioInline(admin.TabularInline):
    model = FotoServicio
    extra = 0
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'rows': 6, 'cols': 40})
        },
    }


class FotoSeguimientoInline(admin.TabularInline):
    model = FotoSeguimiento
    extra = 0
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'rows': 6, 'cols': 40})
        },
    }


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ALL_FIELDS = ['id', 'nombre', 'ver_en_web']
    list_display = ALL_FIELDS
    search_fields = ALL_FIELDS
    list_display_links = ALL_FIELDS
    ordering = ['nombre']
    list_filter = ['ver_en_web']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descuento']
    search_fields = [
        'id', 'nombre', 'nombre', 'descripcion', 'descuento',
        'categoria__nombre', 'fotos__titulo'
    ]
    raw_id_fields = ['categoria']
    ordering = ['nombre', 'categoria__nombre']
    list_filter = ['ver_en_web', 'ver_descuento']
    inlines = (FotoProductoInline,)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'precio']
    search_fields = ['titulo', 'descripcion', 'precio']
    ordering = ['titulo', 'precio']
    inlines = (FotoServicioInline,)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'identificacion', 'primer_nombre', 'segundo_nombre', 'primer_apellido',
        'segundo_apellido', 'fecha_nacimiento', 'correo', 'telefono',
        'direccion'
    ]
    search_fields = [
        'identificacion', 'primer_nombre', 'segundo_nombre', 'primer_apellido',
        'segundo_apellido', 'fecha_nacimiento', 'correo', 'telefono'
    ]
    ordering = ['identificacion', 'primer_nombre', 'segundo_nombre']


class SeguimientoInline(admin.StackedInline):
    model = Seguimiento
    extra = 0


@admin.register(Seguimiento)
class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'porcentaje', 'servicio_cliente']
    search_fields = [
        'titulo', 'descripcion', 'porcentaje',
        'servicio_cliente__cliente__identificacion',
        'servicio_cliente__cliente__primer_nombre',
        'servicio_cliente__cliente__primer_apellido',
        'servicio_cliente__servicio__titulo',
    ]
    raw_id_fields = ['servicio_cliente']
    inlines = (FotoSeguimientoInline,)


@admin.register(ServiciosCliente)
class ServiciosCliente(admin.ModelAdmin):
    list_display = [
        'porcentaje_total', 'estado', 'servicio', 'get_cliente'
    ]
    search_fields = [
        'porcentaje_total', 'estado', 'servicio__titulo',
        'cliente__identificacion', 'cliente__primer_nombre',
        'cliente__primer_apellido'
    ]
    raw_id_fields = ['servicio', 'cliente']
    form = ServicioClienteForm

    def get_cliente(self, obj):
        return f'{obj.cliente.identificacion} {obj.cliente.primer_nombre} ' \
               f'{obj.cliente.primer_apellido}'

    get_cliente.short_description = 'Cliente'
    get_cliente.admin_order_field = 'cliente__primer_apellido'
