# Preparación para la entrevista — Justificación de decisiones

> Respuestas honestas y directas para explicar las decisiones técnicas.
> Tono: jr con criterio, que prioriza entregar algo funcional y claro
> dentro de un plazo muy corto.

## ¿Por qué SQLite y no PostgreSQL (como pedía la prueba)?

"La prueba tenía un plazo muy corto (un fin de semana), así que la mantuve
al mínimo de complejidad para asegurar que todo funcionara. Como uso el ORM
de Django, cambiar a PostgreSQL es solo ajustar el bloque `DATABASES` en
`settings.py` — de hecho lo dejé comentado y listo en el código. Preferí
entregar una app 100% funcional en SQLite a una a medias en PostgreSQL; si
me dan una hora, la monto en Postgres sin tocar los modelos."

## ¿Por qué Django 4.2 y no la versión 5?

"El Python que tenía disponible era 3.9 y Django 5 requiere 3.10+. Django
4.2 es LTS (soporte extendido hasta 2026), así que era la opción estable
correcta para mi entorno. No afecta nada del código de la app."

## ¿Por qué una sola app `gestion`?

"Con cuatro módulos pequeños y muy relacionados (productos, prendas,
clientes, alquileres), separar en varias apps añade estructura sin
beneficio real. Para el tamaño de esta prueba, una sola app con modelos
claros es más fácil de leer y de mantener. Si el proyecto creciera,
separaría por dominio."

## ¿Por qué Bootstrap por CDN y no paquetes npm?

"La prueba pedía Bootstrap 5 para el responsive. Con el CDN no hay que
configurar ningún build ni node_modules, y para un proyecto de este tamaño
es lo práctico. En un proyecto real con más frontend usaría archivos
propios compilados."

## ¿Por qué no JavaScript propio?

"El JS de Bootstrap cubre lo que la prueba pedía (interacción básica).
Prioricé la validación del lado del servidor (la de solapamiento de
alquileres), que es donde realmente está la regla de negocio; la validación
en el cliente es mejora de UX, no seguridad."

## ¿Por qué M2M directo y no un modelo intermedio?

"El alquiler solo necesita saber qué prendas incluye; no hay datos extra
por línea (como descuentos o notas por prenda). Un `ManyToManyField` simple
es suficiente. Si aparecieran datos por prenda alquilada, ahí sí justificaría
un modelo `through`."

## ¿Por qué no imágenes en productos/prendas?

"La especificación decía 'si se considera pertinente'. Manejar imágenes
implica `Pillow`, uploads, carpeta `media/` y configuración extra, y no era
central para la prueba. Preferí un modelo más simple que cumpliera todo lo
obligatorio."

## ¿Por qué validación de solapamiento en el formulario y no en el modelo?

"La regla necesita varias piezas a la vez (prendas del alquiler y el rango
de fechas), y el punto natural de validar eso en Django es el `clean()` del
`ModelForm`, que además muestra el error junto al campo correspondiente.
El ORM hace la consulta de solapamiento en una sola pasada a la base de
datos."

## ¿Por qué vistas genéricas (ListView, CreateView...)?

"CRUD puro es exactamente para lo que existen las vistas genéricas de
Django: menos código propio, menos bugs, convenciones estándar que cualquier
desarrollador de Django entiende al leer."

## ¿Por qué un comando `seed` y no fixtures JSON?

"Un comando en Python es más legible y flexible que un JSON gigante, y me
permite crear datos relacionados y estados coherentes (la prenda alquilada
queda con estado 'alquilada') de una sola pasada."

## ¿Qué haría diferente con más tiempo?

- Migrar a PostgreSQL como pedía la spec original (cambio mínimo).
- Autenticación y permisos (ahora la app es abierta).
- Validaciones extra en el cliente y paginación en los listados.
- Imágenes con `ImageField` y `Pillow`.
- Tests automatizados de la regla de solapamiento.
