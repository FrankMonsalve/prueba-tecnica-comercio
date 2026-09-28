# Bitácora del proyecto

Registro de todas las interacciones/iteraciones, pensado también para un posible cambio de modelo. Últimas entradas arriba.

## Iteración 1 — 2026-09-27

- **Modo:** Architect (solo planificación, sin código).
- **Contexto:** Inicio del proyecto. Prueba técnica para cargo jr. Especificación en español guardada en `.dev/especificacion-original.md`; traducción en `.dev/spec-translation.md`.
- **Decisiones del usuario:**
  - Código, comentarios y docstrings en **español**; conversación en inglés.
  - Lógica e implementación al **mínimo** (perfil jr, sin sobre-ingeniería).
  - SQLite en lugar de PostgreSQL; Bootstrap vía CDN; sin Git por ahora (solo `.gitignore`).
  - Carpeta `.dev/` guarda todo el contexto, specs, planes e iteraciones.
- **Artefactos creados:**
  - `.dev/especificacion-original.md` — spec original.
  - `.dev/spec-translation.md` — traducción de referencia.
  - `.dev/decisiones-tecnicas.md` — desviaciones y por qué.
  - `.dev/bitacora.md` — este archivo.
  - `.dev/plan-implementacion.md` — plan de implementación.
- **Pendiente:** plan aprobado por el usuario → pasar a Code mode.
- **Resultado:** plan aprobado. Decisión del usuario: **una sola app `gestion`** para todos los módulos. Siguiente paso: pasar a Code mode y ejecutar `.dev/plan-implementacion.md`.

## Iteración 2 — 2026-09-27

- **Ajuste de alcance:** el usuario pidió recortar el plan para que la entrega parezca hecha por un jr en un plazo muy corto (básica pero profesional). Recorte v2 aplicado a `.dev/plan-implementacion.md`:
  - Sin responsividad extra ni JS propio (solo Bootstrap 5 CDN).
  - Sin `DetailView` ni vistas de inventario separadas (solo `?estado=` querystrings).
  - Sin `DetalleAlquiler` (M2M directo `Alquiler.prendas`).
  - Un solo seeder (`manage.py seed`), admin simple, sin imágenes ni Pillow.
  - Una sola migración, SQLite.
- **Nota:** se intentó crear los archivos del scaffold en Code mode, pero el modo volvió a Architect (solo permite escribir `.md`). `.gitignore` llegó a crearse; el resto del código queda pendiente hasta volver a Code mode.

## Iteración 3 — 2026-09-27

- **Modo:** Code. Implementación completa del plan v2.
- **Creado:**
  - Scaffold: `manage.py`, `comercio/` (settings con SQLite y PostgreSQL comentado, urls, wsgi, asgi), `requirements.txt`, `.gitignore`.
  - App `gestion`: `models.py` (Producto, Prenda, Cliente, Alquiler con M2M a Prendas), `forms.py` (AlquilerForm con validación de solapamiento), `views.py` (CRUD con vistas genéricas + filtros `?estado=`), `urls.py`, `admin.py` (register simple), `management/commands/seed.py`.
  - Plantillas Bootstrap 5 CDN: `base.html`, listas de producto/prenda/cliente/alquiler, `formulario.html`, `confirmar_borrado.html`.
  - `README.md` en español con instrucciones completas.
- **Ajuste:** el Python del sistema es 3.9 (pip 21.2.4), incompatible con Django 5 → se usa **Django 4.2 LTS** (`django>=4.2,<5.0`). Registrado en `decisiones-tecnicas.md`.
- **Verificado:**
  - `makemigrations` → **una sola migración** `gestion/migrations/0001_initial.py`; `migrate` OK; `check` sin issues.
  - `seed` crea 3 productos, 3 prendas, 1 cliente, 1 alquiler.
  - Prueba de solapamiento: alquiler solapado → error esperado; sin solapamiento → válido.
  - Smoke test HTTP: inicio, productos, prendas, clientes, alquileres (con `?estado=activo`) y alquiler/nuevo → todos 200.
- **Pendiente (futuro):** `git init` + repositorio remoto cuando el usuario lo indique.

## Iteración 4 — 2026-09-28

- **Añadido:** `.dev/preparacion-entrevista.md` — respuestas candidatas para
  justificar en una entrevista cada decisión técnica (SQLite vs PostgreSQL,
  Django 4.2, app única, Bootstrap CDN, M2M sin modelo through, validación en
  el form, vistas genéricas, comando seed, y qué mejoraría con más tiempo).
