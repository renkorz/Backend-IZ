from django.contrib import admin
from .models import (Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo, TipoCategoria, TipoParametro, Parametro, Categoria, Reserva)

# Register your models here.
admin.site.register(Nacionalidad)
admin.site.register(Autor)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Biblioteca)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Prestamo)
admin.site.register(Parametro)
admin.site.register(TipoParametro)
admin.site.register(Categoria)
admin.site.register(TipoCategoria)
admin.site.register(Reserva)