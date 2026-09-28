"""Modelos de la aplicación gestion.

Establecimiento comercial: venta de ropa deportiva, alquiler de
prendas y trajes elegantes, clientes y alquileres.
"""
from django.db import models


class Producto(models.Model):
    """Producto de ropa deportiva para la venta."""

    class Estado(models.TextChoices):
        """Estados posibles de un producto."""
        DISPONIBLE = "disponible", "Disponible"
        AGOTADO = "agotado", "Agotado"

    codigo = models.CharField("código", max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField("descripción", blank=True)
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField("cantidad en inventario", default=0)
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.DISPONIBLE
    )

    class Meta:
        """Metadatos del modelo."""
        verbose_name = "producto"

    def __str__(self):
        """Representación legible del producto."""
        return f"{self.codigo} - {self.nombre}"


class Prenda(models.Model):
    """Prenda para alquiler (sacos, trajes, vestidos, etc.)."""

    class Estado(models.TextChoices):
        """Estados posibles de una prenda."""
        DISPONIBLE = "disponible", "Disponible"
        ALQUILADA = "alquilada", "Alquilada"
        MANTENIMIENTO = "mantenimiento", "En mantenimiento"

    codigo = models.CharField("código", max_length=20, unique=True)
    tipo = models.CharField("tipo de prenda", max_length=50)
    descripcion = models.TextField("descripción", blank=True)
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    precio_alquiler = models.DecimalField(
        "precio de alquiler", max_digits=10, decimal_places=2
    )
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.DISPONIBLE
    )
    fecha_disponibilidad = models.DateField(
        "fecha de disponibilidad", null=True, blank=True
    )

    class Meta:
        """Metadatos del modelo."""
        verbose_name = "prenda"

    def __str__(self):
        """Representación legible de la prenda."""
        return f"{self.codigo} - {self.tipo} ({self.talla})"


class Cliente(models.Model):
    """Cliente del establecimiento."""

    class Estado(models.TextChoices):
        """Estados posibles de un cliente."""
        ACTIVO = "activo", "Activo"
        INACTIVO = "inactivo", "Inactivo"

    nombre = models.CharField("nombre completo", max_length=100)
    documento = models.CharField(
        "documento de identificación", max_length=20, unique=True
    )
    telefono = models.CharField("teléfono", max_length=20)
    correo = models.EmailField("correo electrónico")
    direccion = models.CharField("dirección", max_length=200, blank=True)
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.ACTIVO
    )

    class Meta:
        """Metadatos del modelo."""
        verbose_name = "cliente"

    def __str__(self):
        """Representación legible del cliente."""
        return self.nombre


class Alquiler(models.Model):
    """Alquiler de una o varias prendas a un cliente."""

    class Estado(models.TextChoices):
        """Estados posibles de un alquiler."""
        ACTIVO = "activo", "Activo"
        DEVUELTO = "devuelto", "Devuelto"
        CANCELADO = "cancelado", "Cancelado"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    prendas = models.ManyToManyField(Prenda)
    fecha_alquiler = models.DateField("fecha del alquiler")
    fecha_entrega = models.DateField("fecha de entrega")
    fecha_devolucion_prevista = models.DateField("fecha prevista de devolución")
    valor = models.DecimalField("valor del alquiler", max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.ACTIVO
    )

    class Meta:
        """Metadatos del modelo."""
        verbose_name = "alquiler"

    def __str__(self):
        """Representación legible del alquiler."""
        return f"Alquiler #{self.pk} - {self.cliente}"
