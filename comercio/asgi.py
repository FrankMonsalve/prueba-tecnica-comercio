"""Punto de entrada ASGI para el proyecto comercio."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comercio.settings")

application = get_asgi_application()
