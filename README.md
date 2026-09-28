# Comercio — Gestión de venta de ropa deportiva y alquiler de prendas

Aplicación web desarrollada con Django para la gestión de un establecimiento
comercial que se dedica a la venta de ropa deportiva y alquiler de prendas
y trajes elegantes.

## Funcionalidades

- **Productos para la venta**: registrar, consultar, actualizar y eliminar
  (código, nombre, categoría, descripción, talla, color, precio, cantidad,
  estado).
- **Prendas para alquiler**: módulo independiente con código, tipo,
  descripción, talla, color, precio de alquiler, estado y fecha de
  disponibilidad.
- **Alquileres**: registro de alquileres con cliente, prendas, fechas
  (alquiler, entrega y devolución prevista), valor y estado. Se valida que
  una prenda no quede asignada a dos alquileres activos con fechas que se
  superpongan.
- **Clientes**: registro y consulta de la información básica.
- **Consultas**: listados con filtro por estado (disponibles, alquiladas,
  activos, etc.).
- Interfaz con **Bootstrap 5** (vía CDN).

## Tecnologías

- Python 3.9+
- Django 4.2 (LTS)
- SQLite (base de datos; ver nota sobre PostgreSQL abajo)
- HTML, CSS (Bootstrap 5), JavaScript (el de Bootstrap)

## Instalación y ejecución

1. **Clonar o descargar el proyecto**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd comercio
   ```

2. **Crear y activar el entorno virtual**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # En Windows: .venv\Scripts\activate
   ```

3. **Instalar las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones** (crea la base de datos SQLite)

   ```bash
   python manage.py migrate
   ```

5. **(Opcional) Crear un usuario administrador**

   ```bash
   python manage.py createsuperuser
   ```

6. **(Opcional) Cargar los datos de prueba**

   ```bash
   python manage.py seed
   ```

   Crea 3 productos, 3 prendas, 1 cliente y 1 alquiler de ejemplo.

7. **Ejecutar el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**

   - Aplicación: <http://127.0.0.1:8000/>
   - Administrador de Django: <http://127.0.0.1:8000/admin/>

## Nota sobre la base de datos

Por practicidad para la prueba local se usa **SQLite** (no requiere
instalación ni configuración adicional). El proyecto está preparado para
usar **PostgreSQL**: en `comercio/settings.py` está el bloque de
configuración comentado; basta con instalar `psycopg2-binary`, descomentarlo
y ejecutar `python manage.py migrate`.

## Estructura del proyecto

```
comercio/            Configuración del proyecto Django (settings, urls)
gestion/             App con los módulos del negocio
  models.py          Producto, Prenda, Cliente, Alquiler
  forms.py           Formularios (incluye validación de solapamiento)
  views.py           Vistas genéricas (CRUD)
  urls.py            Rutas de la aplicación
  templates/gestion/ Plantillas (Bootstrap 5)
  management/commands/seed.py   Datos de prueba
```
