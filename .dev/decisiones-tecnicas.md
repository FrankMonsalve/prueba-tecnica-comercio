# Decisiones técnicas — Justificación de desviaciones

> Documento que explica dónde y por qué nos apartamos de las tecnologías pedidas en la especificación, para poder justificarlo (o revertirlo) más adelante.

## Principio general

La prueba es para un cargo **junior**: implementación mínima, sin sobre-ingeniería, librerías prácticas y estándar.

## Desviaciones

| Pedido | Usado | Razón |
|---|---|---|
| PostgreSQL | **SQLite** | Cero configuración, sin servidor, ideal para una prueba local y para que el evaluador la ejecute sin instalar nada. El código usa el ORM de Django, por lo que cambiar a PostgreSQL solo requiere ajustar `DATABASES` en `settings.py` (se dejará la configuración de PostgreSQL comentada/lista). |
| Git | Sin Git por ahora | Decisión del usuario para esta fase. Se incluye `.gitignore` completo desde el inicio; `git init` y el repositorio se harán al final. |

## Librerías (mínimas)

- `django` (4.2 LTS) — framework requerido. Única dependencia.
  - Se fijó 4.2 LTS en lugar de 5.x porque el Python del sistema es 3.9
    (Django 5 requiere Python 3.10+). 4.2 sigue siendo LTS y soporta 3.9.

Nada más: Bootstrap 5 vía CDN (sin paquetes npm), sin JS propio, sin campos de imagen (por tanto sin Pillow), SQLite incluido en Python.

## Diseño de datos (mínimo viable)

- `Producto` (venta): codigo (único), nombre, categoria, descripcion, talla, color, precio, cantidad, estado.
- `Prenda` (alquiler): codigo (único), tipo, descripcion, talla, color, precio_alquiler, estado, fecha_disponibilidad.
- `Cliente`: nombre, documento (único), telefono, correo, direccion, estado.
- `Alquiler`: cliente, fecha_alquiler, fecha_entrega, fecha_devolucion_prevista, valor, estado, `prendas = ManyToManyField(Prenda)`.

**Validación clave de solapamiento:** al crear/editar un alquiler, para cada prenda se comprueba que no exista otro alquiler activo (estado activo) cuyas fechas se solapen con `[fecha_entrega, fecha_devolucion_prevista]`.

## Estados (TextChoices simples)

- Producto: `disponible`, `agotado`.
- Prenda: `disponible`, `alquilada`, `mantenimiento`.
- Alquiler: `activo`, `devuelto`, `cancelado`.
- Cliente: `activo`, `inactivo`.

## Estructura Django

Un solo proyecto `comercio` con apps por módulo (o una app `gestion` única si el usuario prefiere lo más minimalista — pendiente de confirmar).
