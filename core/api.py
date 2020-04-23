from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'servicios', views.ServicioViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'serviciosclientes', views.ServiciosClienteViewSet)
router.register(r'fotos_servicio',views.FotosServicioViewSet)

urlpatterns = router.urls
