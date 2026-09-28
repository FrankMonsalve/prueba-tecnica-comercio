"""Comando para cargar datos de prueba: python manage.py seed."""
from datetime import date, timedelta

from django.core.management.base import BaseCommand

from gestion.models import Alquiler, Cliente, Prenda, Producto


class Command(BaseCommand):
    """Crea datos de prueba para verificar el funcionamiento."""

    help = "Crea datos de prueba (productos, prendas, clientes y un alquiler)."

    def handle(self, *args, **options):
        """Crea los registros de ejemplo si no existen."""
        if Producto.objects.exists():
            self.stdout.write("Ya hay datos, no se carga nada.")
            return

        productos = [
            Producto(
                codigo="CAM-001",
                nombre="Camiseta deportiva",
                categoria="Camisetas",
                talla="M",
                color="Negro",
                precio=45000,
                cantidad=10,
            ),
            Producto(
                codigo="PAN-001",
                nombre="Pantalón deportivo",
                categoria="Pantalones",
                talla="L",
                color="Gris",
                precio=78000,
                cantidad=5,
            ),
            Producto(
                codigo="TEN-001",
                nombre="Tenis para correr",
                categoria="Tenis",
                talla="40",
                color="Blanco",
                precio=190000,
                cantidad=3,
            ),
        ]
        Producto.objects.bulk_create(productos)

        prendas = [
            Prenda(
                codigo="TRA-001",
                tipo="Traje para hombre",
                talla="M",
                color="Azul marino",
                precio_alquiler=120000,
            ),
            Prenda(
                codigo="VES-001",
                tipo="Vestido elegante",
                talla="S",
                color="Rojo",
                precio_alquiler=100000,
            ),
            Prenda(
                codigo="SAC-001",
                tipo="Saco",
                talla="L",
                color="Negro",
                precio_alquiler=60000,
            ),
        ]
        Prenda.objects.bulk_create(prendas)

        cliente = Cliente.objects.create(
            nombre="Juan Pérez",
            documento="1020304050",
            telefono="3001234567",
            correo="juan@example.com",
            direccion="Calle 10 # 5-25",
        )

        alquiler = Alquiler.objects.create(
            cliente=cliente,
            fecha_alquiler=date.today(),
            fecha_entrega=date.today(),
            fecha_devolucion_prevista=date.today() + timedelta(days=3),
            valor=120000,
        )
        alquiler.prendas.add(prendas[0])
        prendas[0].estado = Prenda.Estado.ALQUILADA
        prendas[0].save()

        self.stdout.write(self.style.SUCCESS("Datos de prueba creados."))
