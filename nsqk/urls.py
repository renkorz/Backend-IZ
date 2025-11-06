from django.urls import path, include
from rest_framework import routers
from .views import (NacionalidadViewSet, AutorViewSet, ComunaViewSet, DireccionViewSet, BibliotecaViewSet, LibroViewSet, LectorViewSet, PrestamoViewSet, CategoriaViewSet, TipoCategoriaViewSet, ParametroViewSet, TipoParametroViewSet, ReservaViewSet)

router = routers.DefaultRouter()
router.register(r'nacionalidades', NacionalidadViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'bibliotecas', BibliotecaViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'lectores', LectorViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'tipocategoria', TipoCategoriaViewSet)
router.register(r'parametro', ParametroViewSet)
router.register(r'tipoparametro', TipoParametroViewSet)
router.register(r'reserva', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]