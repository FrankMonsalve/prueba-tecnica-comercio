"""Configuración de la app gestion."""
from django.apps import AppConfig


class GestionConfig(AppConfig):
    """App con los módulos del establecimiento comercial."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "gestion"
