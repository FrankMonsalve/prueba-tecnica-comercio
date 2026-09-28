"""
Configuración del proyecto Django "comercio".

Gestión de un establecimiento comercial: venta de ropa deportiva
y alquiler de prendas y trajes elegantes.
"""

from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# ADVERTENCIA: clave de desarrollo, cambiar en producción.
SECRET_KEY = "django-insecure-cambiar-en-produccion"

# ADVERTENCIA: en producción debe ser False.
DEBUG = True

ALLOWED_HOSTS = []


# Aplicaciones instaladas

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps del proyecto
    "gestion",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "comercio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "comercio.wsgi.application"


# Base de datos

# Se usa SQLite por practicidad para la prueba técnica local.
# Para usar PostgreSQL (lo pedido en la especificación original):
# 1. Instalar: pip install psycopg2-binary
# 2. Comentar el bloque de SQLite y descomentar el de PostgreSQL.
# 3. Crear la base de datos en PostgreSQL y ejecutar las migraciones.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Configuración de PostgreSQL (descomentar para usarla):
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "comercio",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }


# Validación de contraseñas

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internacionalización (español, zona de Colombia)

LANGUAGE_CODE = "es"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_TZ = True


# Archivos estáticos

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
