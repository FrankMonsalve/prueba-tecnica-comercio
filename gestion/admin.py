"""Registro de modelos en el administrador de Django."""
from django.contrib import admin

from .models import Alquiler, Cliente, Prenda, Producto

admin.site.register(Producto)
admin.site.register(Prenda)
admin.site.register(Cliente)
admin.site.register(Alquiler)
