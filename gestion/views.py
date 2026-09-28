"""Vistas de la aplicación gestion.

CRUD básico con vistas genéricas de Django para productos,
prendas, clientes y alquileres.
"""
from django.urls import reverse_lazy
from django.views import generic

from .forms import AlquilerForm, ClienteForm, PrendaForm, ProductoForm
from .models import Alquiler, Cliente, Prenda, Producto


# --- Productos para la venta ---


class ProductoListView(generic.ListView):
    """Listado de productos, con filtro opcional por estado (?estado=)."""

    model = Producto
    template_name = "gestion/producto_lista.html"

    def get_queryset(self):
        """Filtra por estado si llega por querystring."""
        qs = super().get_queryset()
        estado = self.request.GET.get("estado")
        if estado:
            qs = qs.filter(estado=estado)
        return qs


class ProductoCreateView(generic.CreateView):
    """Crear un producto."""

    model = Producto
    form_class = ProductoForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("producto_lista")


class ProductoUpdateView(generic.UpdateView):
    """Editar un producto."""

    model = Producto
    form_class = ProductoForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("producto_lista")


class ProductoDeleteView(generic.DeleteView):
    """Eliminar un producto."""

    model = Producto
    template_name = "gestion/confirmar_borrado.html"
    success_url = reverse_lazy("producto_lista")


# --- Prendas para alquiler ---


class PrendaListView(generic.ListView):
    """Listado de prendas, con filtro opcional por estado (?estado=)."""

    model = Prenda
    template_name = "gestion/prenda_lista.html"

    def get_queryset(self):
        """Filtra por estado si llega por querystring."""
        qs = super().get_queryset()
        estado = self.request.GET.get("estado")
        if estado:
            qs = qs.filter(estado=estado)
        return qs


class PrendaCreateView(generic.CreateView):
    """Crear una prenda."""

    model = Prenda
    form_class = PrendaForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("prenda_lista")


class PrendaUpdateView(generic.UpdateView):
    """Editar una prenda."""

    model = Prenda
    form_class = PrendaForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("prenda_lista")


class PrendaDeleteView(generic.DeleteView):
    """Eliminar una prenda."""

    model = Prenda
    template_name = "gestion/confirmar_borrado.html"
    success_url = reverse_lazy("prenda_lista")


# --- Clientes ---


class ClienteListView(generic.ListView):
    """Listado de clientes."""

    model = Cliente
    template_name = "gestion/cliente_lista.html"


class ClienteCreateView(generic.CreateView):
    """Crear un cliente."""

    model = Cliente
    form_class = ClienteForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("cliente_lista")


class ClienteUpdateView(generic.UpdateView):
    """Editar un cliente."""

    model = Cliente
    form_class = ClienteForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("cliente_lista")


class ClienteDeleteView(generic.DeleteView):
    """Eliminar un cliente."""

    model = Cliente
    template_name = "gestion/confirmar_borrado.html"
    success_url = reverse_lazy("cliente_lista")


# --- Alquileres ---


class AlquilerListView(generic.ListView):
    """Listado de alquileres, con filtro opcional por estado (?estado=)."""

    model = Alquiler
    template_name = "gestion/alquiler_lista.html"

    def get_queryset(self):
        """Filtra por estado si llega por querystring."""
        qs = super().get_queryset().select_related("cliente")
        estado = self.request.GET.get("estado")
        if estado:
            qs = qs.filter(estado=estado)
        return qs


class AlquilerCreateView(generic.CreateView):
    """Registrar un alquiler."""

    model = Alquiler
    form_class = AlquilerForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("alquiler_lista")


class AlquilerUpdateView(generic.UpdateView):
    """Editar un alquiler (por ejemplo, cambiar su estado)."""

    model = Alquiler
    form_class = AlquilerForm
    template_name = "gestion/formulario.html"
    success_url = reverse_lazy("alquiler_lista")


class AlquilerDeleteView(generic.DeleteView):
    """Eliminar un alquiler."""

    model = Alquiler
    template_name = "gestion/confirmar_borrado.html"
    success_url = reverse_lazy("alquiler_lista")
