from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Nacionalidad, Autor, Comuna,
    Direccion, Biblioteca, Libro,
    Lector, Prestamo
)

from .serializers import (
    NacionalidadSerializer, AutorSerializer, ComunaSerializer,
    DireccionSerializer, BibliotecaSerializer, LibroSerializer,
    LectorSerializer, PrestamoSerializer
)

# Create your views here.

def pagina_inicio(request):
    return render(request, 'home/inicio.html')

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class =  ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer