# Tech Test Specification — English Translation

> Reference translation of `.dev/especificacion-original.md` for working context. Code, comments and docs will be in Spanish; our conversation stays in English.

## 1. Goal

Build a web application to manage a business that sells sportswear and rents formal wear (suits, elegant garments). The app must organize both sale products and rental garments.

## 2. Required technologies

Python, Django, PostgreSQL, HTML, CSS3, Bootstrap 5, JavaScript, Git

## 3. Expected features

### Sale product management (CRUD)

Products: t-shirts, sport pants, hoodies, jackets, sneakers, etc.

Fields: code/reference, name, category, description, size, color, price, stock quantity, status, optional image.

### Rental garment management (CRUD, separate module)

Garments: blazers/suit jackets, ties, men's suits, women's elegant dresses, etc.

Fields: code/reference, garment type, description, size, color, rental price, status (available / rented / maintenance), availability date, optional image.

### Rental management

Register a rental with: client, garment(s) rented, rental date, delivery date, expected return date, rental value, rental status.

Key rule: a garment cannot be assigned to two active rentals with overlapping dates. Must check garment status to prevent this.

### Basic client management

Register and view clients: full name, ID document, phone, email, address, status.

### Inventory & queries

Simple listings of: products for sale, stock, garments available for rent, garments currently rented, registered rentals, basic client info.

### Design

Clear, organized, responsive UI (desktop, laptop, tablet, phone). Use Bootstrap; use JavaScript for UX improvements, validations, filters, confirmation messages.

### Database

PostgreSQL per spec (see deviations in `.dev/decisiones-tecnicas.md`). Config + migrations included. Seed/test data recommended.

### Git repo / README

Full source in a Git repo with a detailed README: clone, virtualenv, dependencies, env vars, DB config, migrations, superuser, seed data, run dev server, test the app.

### Best practices evaluated

Project structure, models/views/forms/URLs usage, DB design, code quality, Git usage, validations/error handling, basic security, responsive design, usability, documentation quality.

## 4. Deliverables

Git repo URL, full source, README.md, requirements.txt, DB config, migrations, test data.
