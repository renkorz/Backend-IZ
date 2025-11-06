from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .models import (Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo, Categoria, TipoCategoria, Parametro, TipoParametro, Reserva)
from .serializers import (NacionalidadSerializer, AutorSerializer, ComunaSerializer,DireccionSerializer, BibliotecaSerializer, LibroSerializer,LectorSerializer, PrestamoSerializer, CategoriaSerializer, TipoCategoriaSerializer, ParametroSerializer, TipoParametroSerializer, ReservaSerializer)

# Create your views here.

def logout_view(request):
    logout(request) # Cierra y limpia la data de la sesión del usuario.
    return redirect('login') # Redirige al login

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Registro exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(
                request, "No ha sido posible registrar. Por favor revise el formulario por errores.")
        return render(request, 'registro.html', {'form': form})

@login_required
def pagina_inicio(request):
    request.session['mensaje_bienvenida'] = '¡Bienvenido!' # Para almacenar los datos de la sesión
    mensaje_bienvenida = request.session.get('mensaje_bienvenida') # Obetener informacion desde la sesión
    if 'mensaje_bienvenida' in request.session: # Remover información en sesión
        del request.session['mensaje_bienvenida']
    return render(request, 'home/base.html', {'message': mensaje_bienvenida})
        

class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class AutorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comuna.objects.all()
    serializer_class =  ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LectorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer

class ParametroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer

class TipoParametroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoParametro.objects.all()
    serializer_class = TipoParametroSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer