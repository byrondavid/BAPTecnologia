from django.contrib import admin

# Register your models here.
from core.models import Categoria, Producto, Foto, Servicio, ServiciosCliente


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ALL_FIELDS = ['id', 'nombre', 'ver_en_web']
    list_display = ALL_FIELDS
    search_fields = ALL_FIELDS
    list_display_links = ALL_FIELDS
    ordering = ['nombre']
    list_filter = ['ver_en_web']


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'foto', 'fecha_registro']
    list_display_links = ['id', 'titulo', 'foto', 'fecha_registro']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descuento']
    search_fields = [
        'id', 'nombre', 'nombre', 'descripcion', 'descuento',
        'categoria__nombre', 'fotos__titulo'
    ]
    filter_horizontal = ['fotos']
    raw_id_fields = ['categoria']
    ordering = ['nombre', 'categoria__nombre']
    list_filter = ['ver_en_web', 'ver_descuento']


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'precio']
    search_fields = ['titulo', 'descripcion', 'precio']
    raw_id_fields = ['fotos']
    ordering = ['titulo', 'precio']


@admin.register(ServiciosCliente)
class ServiciosCliente(admin.ModelAdmin):
    list_display = [
        'porcentaje_total', 'estado', 'servicio', 'cliente'
    ]
    raw_id_fields = ['servicio']
