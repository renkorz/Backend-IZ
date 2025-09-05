from django.urls import path, include
from rest_framework import routers
from .views import (
    NacionalidadViewSet, AutorViewSet, ComunaViewSet,
    DireccionViewSet, BibliotecaViewSet, LibroViewSet,
    LectorViewSet, PrestamoViewSet
)

router = routers.DefaultRouter()
router.register(r'nacionalidades', NacionalidadViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'bibliotecas', BibliotecaViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'lectores', LectorViewSet)
router.register(r'prestamos', PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]