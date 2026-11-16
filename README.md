
# ORION Maintenance Lite

**Aplicación web para la gestión de activos y órdenes de trabajo de mantenimiento.**

Proyecto desarrollado como parte de la prueba técnica para aprendices y practicantes SENA.

---

## 1. Descripción del proyecto

ORION Maintenance Lite es una aplicación web que permite administrar activos y gestionar órdenes de trabajo relacionadas con su mantenimiento.

El sistema centraliza el registro y consulta de activos, permite crear órdenes de trabajo asociadas a ellos y controlar el avance de cada orden mediante estados.

La solución está construida con una arquitectura separada en frontend y backend, conectada a una base de datos PostgreSQL.

## 2. Objetivo

Desarrollar una aplicación web funcional que permita:

- Registrar y consultar activos.
- Editar la información de los activos.
- Desactivar activos sin eliminarlos físicamente.
- Crear órdenes de trabajo asociadas a activos.
- Consultar las órdenes de trabajo.
- Gestionar el estado y la prioridad de las órdenes.
- Conservar la información mediante una base de datos.

## 3. Tecnologías utilizadas

### Backend

- Python.
- FastAPI.
- SQLAlchemy.
- Pydantic.
- PostgreSQL.
- Alembic.
- Pytest.
- Uvicorn.

### Frontend

- React 19.
- Vite.
- JavaScript.
- Axios.
- React Router DOM.
- CSS.

### Herramientas de desarrollo

- Visual Studio Code.
- Git.
- GitHub.
- Supabase para PostgreSQL.

## 4. Estructura del proyecto

La organización del repositorio es la siguiente:

```text
PruebaTecnicaSENA/
│
├── backend/
│   ├── alembic/
│   │   └── versions/
│   ├── app/
│   │   ├── core/
│   │   ├── exceptions/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   │   ├── integration/
│   │   └── unit/
│   ├── .env
│   ├── .env.example
│   ├── alembic.ini
│   ├── pytest.ini
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   ├── .env
│   ├── package.json
│   └── README.md
│
├── docs/
│   ├── fase-02-diseno-tecnico/
│   │   └── DISENO_TECNICO.md
│   ├── fase-03-desarrollo/
│   │   └── DESARROLLO.md
│   ├── fase-04-pruebas/
│   │   └── PLAN_PRUEBAS.md
│   └── fase-05-integracion/
│       └── INTEGRACION.md
│
├── BACKLOG.md
├── CHANGELOG.md
├── GUIA_EJECUCION.md
├── REFINEMENT.md
├── README.md
└── .gitignore
```

## 5. Funcionalidades implementadas

### 5.1 Gestión de activos

- Registrar activos.
- Consultar el listado de activos.
- Consultar activos individualmente.
- Editar la información de los activos.
- Desactivar activos.
- Conservar los registros desactivados.
- Validar los campos obligatorios.
- Asignar identificadores y fechas de registro automáticamente.

Cada activo contiene:

- Identificador.
- Nombre.
- Tipo.
- Ubicación.
- Estado.
- Fecha de registro.

### 5.2 Gestión de órdenes de trabajo

- Crear órdenes de trabajo.
- Consultar el listado de órdenes.
- Consultar órdenes individualmente.
- Asociar órdenes con activos existentes.
- Asignar prioridades.
- Actualizar el estado de las órdenes.
- Validar las reglas de negocio.

Cada orden contiene:

- Identificador.
- Activo asociado.
- Título.
- Descripción.
- Prioridad.
- Estado.
- Fecha de creación.

### 5.3 Estados y prioridades

Las prioridades disponibles son:

- Baja.
- Media.
- Alta.

Los estados disponibles son:

- Pendiente.
- En progreso.
- Finalizada.

El flujo permitido para las órdenes es:

```text
Pendiente
    |
    v
En progreso
    |
    v
Finalizada
```

No se permiten saltos ni retrocesos en el flujo de estados.

## 6. Requisitos para la instalación

Antes de ejecutar el proyecto se necesita:

- Python.
- pip.
- Node.js.
- npm.
- Una base de datos PostgreSQL.
- Git.

## 7. Instalación y configuración del backend

### 7.1 Ingresar a la carpeta

Desde la raíz del repositorio:

```bash
cd backend
```

### 7.2 Crear el entorno virtual

```bash
python -m venv .venv
```

### 7.3 Activar el entorno virtual

En Git Bash:

```bash
source .venv/Scripts/activate
```

### 7.4 Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 7.5 Configurar las variables de entorno

Crear un archivo llamado `.env` dentro de la carpeta `backend`.

Tomar como referencia el archivo `.env.example`.

Configurar las siguientes variables:

```env
ENVIRONMENT=development
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST:5432/DATABASE?sslmode=require
FRONTEND_ORIGIN=http://localhost:5173
```

Reemplazar los valores de ejemplo por los datos correspondientes a la base de datos PostgreSQL.

**Importante:** No compartir ni subir el archivo `.env` a GitHub. Las credenciales deben mantenerse privadas.

### 7.6 Ejecutar las migraciones

Desde la carpeta `backend`:

```bash
python -m alembic upgrade head
```

Este comando aplica las migraciones y prepara las tablas de la base de datos.

### 7.7 Iniciar el backend

```bash
uvicorn app.main:app --reload
```

El backend estará disponible en:

http://127.0.0.1:8000

La documentación interactiva de la API estará disponible en:

http://127.0.0.1:8000/docs

## 8. Instalación y configuración del frontend

Abrir una segunda terminal.

### 8.1 Ingresar a la carpeta

Desde la raíz del repositorio:

```bash
cd frontend
```

### 8.2 Instalar las dependencias

```bash
npm install
```

### 8.3 Configurar las variables de entorno

Crear un archivo `.env` dentro de la carpeta `frontend`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

Esta variable establece la dirección base para las solicitudes al backend.

### 8.4 Iniciar el frontend

```bash
npm run dev
```

La aplicación estará disponible en:

http://localhost:5173/

## 9. Pruebas

El proyecto utiliza Pytest para ejecutar pruebas automatizadas sobre los servicios y los endpoints del backend.

### 9.1 Ejecutar las pruebas

Desde la carpeta `backend`, con el entorno virtual activado:

```bash
python -m pytest -v
```

### 9.2 Resultado obtenido

Se ejecutaron satisfactoriamente:

- 18 pruebas unitarias.
- 6 pruebas de integración.
- 24 pruebas exitosas en total.

También se realizaron validaciones manuales de las funcionalidades desde la interfaz web.

### 9.3 Verificación del frontend

Para generar la compilación de producción:

```bash
npm run build
```

Para ejecutar el análisis estático:

```bash
npm run lint
```

## 10. Endpoints principales de la API

La API expone los siguientes endpoints:

### Activos

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/assets` | Consultar activos |
| POST | `/api/assets` | Registrar activo |
| GET | `/api/assets/{asset_id}` | Consultar un activo |
| PUT | `/api/assets/{asset_id}` | Editar activo |
| PATCH | `/api/assets/{asset_id}/deactivate` | Desactivar activo |

### Órdenes de trabajo

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/work-orders` | Consultar órdenes |
| POST | `/api/work-orders` | Crear orden |
| GET | `/api/work-orders/{work_order_id}` | Consultar una orden |
| PATCH | `/api/work-orders/{work_order_id}/status` | Actualizar estado |

### Verificación

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/health` | Verificar estado de la API |

## 11. Base de datos

El proyecto utiliza PostgreSQL como sistema de gestión de base de datos.

Se implementaron dos entidades principales:

### Assets

Almacena la información de los activos registrados.

### Work Orders

Almacena las órdenes de trabajo y su relación con los activos.

La relación entre ambas entidades se establece mediante la clave foránea `asset_id`.

SQLAlchemy permite gestionar la comunicación con la base de datos y Alembic administra las migraciones del esquema.

## 12. Documentación adicional

El repositorio contiene documentos que complementan el desarrollo de la solución:

| Archivo | Descripción |
|---|---|
| `BACKLOG.md` | Organización y priorización de actividades |
| `REFINEMENT.md` | Análisis y refinamiento de requerimientos |
| `GUIA_EJECUCION.md` | Guía de ejecución de la prueba técnica |
| `CHANGELOG.md` | Registro cronológico de cambios |
| `docs/fase-02-diseno-tecnico/DISENO_TECNICO.md` | Diseño técnico de la solución |
| `docs/fase-03-desarrollo/DESARROLLO.md` | Documentación del desarrollo |
| `docs/fase-04-pruebas/PLAN_PRUEBAS.md` | Plan y resultados de pruebas |
| `docs/fase-05-integracion/INTEGRACION.md` | Documentación de la integración |

## 13. Limitaciones conocidas

La versión actual está enfocada en cumplir las funcionalidades principales de la prueba técnica.

No incluye todavía:

- Autenticación y autorización de usuarios.
- Administración de responsables de las órdenes.
- Historial de cambios.
- Búsqueda avanzada.
- Filtros avanzados.
- Panel de estadísticas.
- Despliegue público.

## 14. Mejoras futuras

Como posibles mejoras se plantean:

- Implementar autenticación y roles de usuario.
- Incorporar responsables para las órdenes de trabajo.
- Agregar historial de modificaciones.
- Implementar filtros y búsquedas.
- Incorporar indicadores y estadísticas.
- Mejorar las opciones de administración.
- Implementar integración y entrega continua.
- Evaluar el despliegue de la aplicación en un entorno público.

## 15. Control de versiones

El proyecto utiliza Git y GitHub para el control de versiones.

Se realizaron commits progresivos para registrar los avances del desarrollo y la documentación.

Repositorio:

https://github.com/marianacastellanosparra/PruebaTecnicaSENA

## 16. Autoría y contexto

**Proyecto:** ORION Maintenance Lite.

**Contexto:** Prueba técnica para aprendices y practicantes SENA.

**Periodo de trabajo:** 14 y 15 de noviembre de 2026.

**Versión:** 1.0.0.

---

**ORION Maintenance Lite - Gestión de activos y órdenes de trabajo de mantenimiento.**
