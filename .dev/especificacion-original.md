# Prueba técnica — Especificación original (Español)

> Copia fiel de la especificación entregada por la empresa. No modificar.

Como parte del proceso de selección de nuestra empresa para el cargo de Desarrollador de Software, se solicita realizar una prueba técnica orientada al desarrollo de una aplicación web responsive utilizando las tecnologías y conocimientos relacionados con el cargo.

## 1. Objetivo del cargo

Desarrollar una aplicación web para la gestión de un establecimiento comercial que se dedica a la venta de ropa deportiva y al alquiler de prendas y trajes elegantes.

La aplicación deberá permitir gestionar de manera organizada la información relacionada con los productos disponibles para la venta y las prendas destinadas al alquiler.

## 2. Tecnologías requeridas

Python - Django - Postgresql - HTML - CSS3 - Bootstrap 5 - Javascript - Git

## 3. Funcionalidades esperadas

La aplicación deberá contemplar, como mínimo, los siguientes módulos o funcionalidades:

### Gestión de productos para la venta

Deberá permitir registrar, consultar, actualizar y eliminar productos relacionados con ropa, por ejemplo: camisetas, pantalones deportivos, sudaderas, chaquetas, tenis y otros pertinentes.

Cada producto podrá manejar información como:

- Código o referencia
- Nombre
- Categoría
- Descripción
- Talla
- Color
- Precio
- Cantidad disponible en inventario
- Estado del producto
- Imagen, si se considera pertinente

### Gestión de Prendas para alquiler

Módulo independiente para administrar las prendas destinadas al alquiler, por ejemplo: sacos, corbatas, trajes para hombre, vestidos elegantes para mujer y otras prendas relacionadas.

Para cada prenda se podrá manejar información como:

- Código o referencia
- Tipo de prenda
- Descripción
- Talla
- Color
- Precio de alquiler
- Estado: disponible, alquilada, en mantenimiento, etc.
- Fecha de disponibilidad
- Imagen, si se considera pertinente

### Gestión de alquiler

Registrar un alquiler indicando, como mínimo:

- Cliente
- Prenda o prendas alquiladas
- Fecha del alquiler
- Fecha de entrega
- Fecha prevista de devolución
- Valor del alquiler
- Estado del alquiler

Se deberá poder consultar el estado de las prendas para evitar que una misma prenda sea asignada a dos alquileres activos en fechas que se superpongan.

### Gestión básica de clientes

Módulo para registrar y consultar la información básica de los clientes:

- Nombre completo
- Documento de identificación
- Teléfono
- Correo electrónico
- Dirección
- Estado

### Inventarios y consultas

Consultas sencillas de:

- Productos disponibles para la venta
- Existencias disponibles
- Prendas disponibles para alquiler
- Prendas actualmente alquiladas
- Alquileres registrados
- Información básica de clientes

### Diseño de la aplicación

Interfaz clara, organizada y responsive (escritorio, portátiles, tabletas, teléfonos). Uso de Bootstrap y JavaScript para interacción, validaciones, filtros y mensajes de confirmación.

### Bases de Datos

La información deberá almacenarse en PostgreSQL. El proyecto incluirá configuración para crear la base de datos y ejecutar las migraciones de Django. Se recomienda incluir datos de prueba.

### Repositorio Git

Código publicado en un repositorio Git con un README.md detallado (descarga, entorno virtual, dependencias, variables de entorno, PostgreSQL, migraciones, superusuario, datos de prueba, servidor de desarrollo).

### Buenas prácticas

Organización y estructura del proyecto, correcto uso de modelos/vistas/formularios/URLs, diseño de la base de datos, uso de PostgreSQL, calidad y legibilidad del código, uso de Git, validaciones y errores, seguridad básica, diseño responsive, usabilidad, y claridad de la documentación.

### Entrega

- URL del repositorio Git
- Código fuente completo
- README.md con instrucciones
- requirements.txt
- Configuración de PostgreSQL
- Migraciones
- Datos de prueba
