from rest_framework import serializers
from .models import (Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo, TipoCategoria, TipoParametro, Parametro, Categoria, Reserva)
from datetime import date
from dateutil.relativedelta import relativedelta

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class LectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = '__all__'
    
    def validate_fecha_nacimiento (self, value):
        today = date.today()
        fecha_mayoria_edad = today - relativedelta(years=18)
        if value > fecha_mayoria_edad:
            raise serializers.ValidationError("El lector debe ser mayor de 18 años.")
        return value

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TipoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCategoria
        fields = '__all__'

class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro
        fields = '__all__'

class TipoParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoParametro
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'