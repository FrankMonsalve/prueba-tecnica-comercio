"""URLs de la aplicación gestion."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductoListView.as_view(), name="inicio"),
    # Productos para la venta
    path("productos/", views.ProductoListView.as_view(), name="producto_lista"),
    path("productos/nuevo/", views.ProductoCreateView.as_view(), name="producto_crear"),
    path(
        "productos/<int:pk>/editar/",
        views.ProductoUpdateView.as_view(),
        name="producto_editar",
    ),
    path(
        "productos/<int:pk>/eliminar/",
        views.ProductoDeleteView.as_view(),
        name="producto_eliminar",
    ),
    # Prendas para alquiler
    path("prendas/", views.PrendaListView.as_view(), name="prenda_lista"),
    path("prendas/nuevo/", views.PrendaCreateView.as_view(), name="prenda_crear"),
    path(
        "prendas/<int:pk>/editar/",
        views.PrendaUpdateView.as_view(),
        name="prenda_editar",
    ),
    path(
        "prendas/<int:pk>/eliminar/",
        views.PrendaDeleteView.as_view(),
        name="prenda_eliminar",
    ),
    # Clientes
    path("clientes/", views.ClienteListView.as_view(), name="cliente_lista"),
    path("clientes/nuevo/", views.ClienteCreateView.as_view(), name="cliente_crear"),
    path(
        "clientes/<int:pk>/editar/",
        views.ClienteUpdateView.as_view(),
        name="cliente_editar",
    ),
    path(
        "clientes/<int:pk>/eliminar/",
        views.ClienteDeleteView.as_view(),
        name="cliente_eliminar",
    ),
    # Alquileres
    path("alquileres/", views.AlquilerListView.as_view(), name="alquiler_lista"),
    path(
        "alquileres/nuevo/", views.AlquilerCreateView.as_view(), name="alquiler_crear"
    ),
    path(
        "alquileres/<int:pk>/editar/",
        views.AlquilerUpdateView.as_view(),
        name="alquiler_editar",
    ),
    path(
        "alquileres/<int:pk>/eliminar/",
        views.AlquilerDeleteView.as_view(),
        name="alquiler_eliminar",
    ),
]
