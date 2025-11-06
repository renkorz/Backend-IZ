from django.db import models
from rut_chile import rut_chile
from django.forms import ValidationError
import datetime

ahora = datetime.datetime.now

# Create your models here.

def validar_rut(rut):
    valido = rut_chile.is_valid_rut(rut)
    if valido == False:
        raise ValidationError('RUT inválido.')

def validar_mayoria_edad(fecha_nacimiento):
    fecha_actual = datetime.datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    if edad < 18:
        raise ValidationError('El lector debe ser mayor de edad.')

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, blank=False)
    nacionalidad = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nacionalidad
    
class OpcionesGenero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMENINO = 'F', 'Femenino'
    
class Autor(models.Model):
    id_nacionalidad = models.ForeignKey(
        Nacionalidad, on_delete=models.CASCADE, blank=True)
    nombre = models.CharField(max_length=250, blank=False)
    pseudonimo = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    genero = models.CharField(max_length=1, choices=OpcionesGenero.choices, default=OpcionesGenero.MASCULINO)
    imagen_autor = models.URLField(blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.pseudonimo != '':
            return self.pseudonimo
        else:
            return self.nombre

class Comuna(models.Model):
    codigo = models.CharField(max_length=5, blank=False, unique=True)
    comuna = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comuna

class Direccion(models.Model):
    id_comuna = models.ForeignKey(
        Comuna, on_delete=models.CASCADE, blank=False)
    calle = models.CharField(max_length=50, blank=True, default='')
    numero = models.CharField(max_length=10, blank=True, default='')
    departamento = models.CharField(max_length=10, blank=True)
    detalles = models.TextField(blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

class Biblioteca(models.Model):
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, blank=True)
    nombre = models.CharField(max_length=100, blank=False)
    web = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

class Lector(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, blank=False)
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, blank=True)
    rut_lector = models.CharField(max_length=12, blank=False, unique=True, validators=[validar_rut])
    nombre = models.CharField(max_length=255, null=False)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateField(blank=True, default=None, validators=[validar_mayoria_edad])
    genero = models.CharField(max_length=1, choices=OpcionesGenero.choices,default=OpcionesGenero.MASCULINO)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre}{self.rut_lector}'

class TipoCategoria(models.Model):
    tipo_categoria = models.CharField(max_length=50, blank=False)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tipo_categoria
    
class Categoria(models.Model):
    id_tipo_categoria = models.ForeignKey(
        TipoCategoria, on_delete=models.CASCADE, blank=False)
    categoria = models.CharField(max_length=255, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.categoria

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, blank=False)
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=True)
    id_autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, blank=False)
    titulo = models.CharField(max_length=255, blank=False)
    paginas = models.IntegerField(blank=False)
    copias = models.IntegerField(blank=False)
    ubicacion = models.CharField(max_length=255, blank=False)
    fisico = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    id_libro = models.ForeignKey(
        Libro, on_delete=models.CASCADE, blank=False)
    id_lector = models.ForeignKey(
        Lector, on_delete=models.CASCADE, blank=False)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=False)
    fecha_retorno = models.DateTimeField(blank=True)

class Reserva(models.Model):
    class TipoReservaciones(models.IntegerChoices):
        NO_RESERVA = 0, 'Sin reserva'
        SEMANA = 1, '1 Semana'
        MES = 2, '1 Mes'
        SEMESTRE = 3, '1 Semestre'
    id_libro = models.ForeignKey(
        Libro, on_delete=models.CASCADE, blank=False)
    id_lector = models.ForeignKey(
        Lector, on_delete=models.CASCADE, blank=False)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    tipo_reserva = models.IntegerField(choices=TipoReservaciones.choices, default=TipoReservaciones.NO_RESERVA)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id_lector}{self.id_libro}{self.fecha_reserva}'

class TipoParametro(models.Model):
    tipo_parametro = models.CharField(max_length=50, blank=False)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

class Parametro(models.Model):
    id_tipo_parametro = models.ForeignKey(
        TipoParametro, on_delete=models.CASCADE, blank=True)
    clave_parametro = models.CharField(max_length=100, blank=False)
    valor_parametro = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)