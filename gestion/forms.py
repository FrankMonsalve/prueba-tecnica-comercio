"""Formularios de la aplicación gestion."""
from django import forms

from .models import Alquiler, Cliente, Prenda, Producto


class ProductoForm(forms.ModelForm):
    """Formulario para crear y editar productos de venta."""

    class Meta:
        """Configuración del formulario."""
        model = Producto
        fields = "__all__"


class PrendaForm(forms.ModelForm):
    """Formulario para crear y editar prendas de alquiler."""

    class Meta:
        """Configuración del formulario."""
        model = Prenda
        fields = "__all__"
        widgets = {
            "fecha_disponibilidad": forms.DateInput(attrs={"type": "date"}),
        }


class ClienteForm(forms.ModelForm):
    """Formulario para crear y editar clientes."""

    class Meta:
        """Configuración del formulario."""
        model = Cliente
        fields = "__all__"


class AlquilerForm(forms.ModelForm):
    """Formulario para crear y editar alquileres.

    Valida que las fechas sean coherentes y que ninguna prenda
    esté asignada a otro alquiler activo con fechas que se solapen.
    """

    class Meta:
        """Configuración del formulario."""
        model = Alquiler
        fields = "__all__"
        widgets = {
            "fecha_alquiler": forms.DateInput(attrs={"type": "date"}),
            "fecha_entrega": forms.DateInput(attrs={"type": "date"}),
            "fecha_devolucion_prevista": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        """Valida fechas y solapamiento de prendas entre alquileres activos."""
        datos = super().clean()
        fecha_entrega = datos.get("fecha_entrega")
        fecha_devolucion = datos.get("fecha_devolucion_prevista")
        prendas = datos.get("prendas")

        # Las fechas deben tener sentido
        if fecha_entrega and fecha_devolucion and fecha_entrega > fecha_devolucion:
            self.add_error(
                "fecha_devolucion_prevista",
                "La fecha de devolución no puede ser anterior a la de entrega.",
            )

        # Regla clave: una prenda no puede estar en dos alquileres
        # activos con fechas que se superpongan.
        if fecha_entrega and fecha_devolucion and prendas:
            conflictos = Alquiler.objects.filter(
                prendas__in=prendas,
                estado=Alquiler.Estado.ACTIVO,
                fecha_entrega__lte=fecha_devolucion,
                fecha_devolucion_prevista__gte=fecha_entrega,
            ).exclude(pk=self.instance.pk)
            if conflictos.exists():
                self.add_error(
                    "prendas",
                    "Una de las prendas ya está asignada a un alquiler "
                    "activo con fechas que se superpongan.",
                )

        return datos
