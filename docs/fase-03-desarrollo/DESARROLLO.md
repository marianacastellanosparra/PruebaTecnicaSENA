# ORION Maintenance Lite
# Fase 3: Desarrollo

## 1. Descripción

Se desarrolló una aplicación web para gestionar activos y órdenes de trabajo de mantenimiento, utilizando un backend con FastAPI y un frontend con React y Vite.

## 2. Tecnologías

### Backend
- Python 3.14.3.
- FastAPI.
- SQLAlchemy.
- Pydantic.
- PostgreSQL y Supabase.
- Alembic.
- Pytest.

### Frontend
- React 19.
- Vite.
- JavaScript.
- Axios.
- React Router DOM.
- CSS.

### Herramientas
- Git y GitHub.
- Visual Studio Code.

## 3. Backend

Se implementaron modelos, esquemas, repositorios, servicios y routers para gestionar activos y órdenes de trabajo.

Funcionalidades:
- Registrar y consultar activos.
- Consultar activos por identificador.
- Editar activos.
- Desactivar activos sin eliminarlos.
- Crear y consultar órdenes de trabajo.
- Asociar órdenes con activos existentes.
- Actualizar estados de las órdenes.
- Validar datos y controlar errores.

## 4. Base de datos

Se utiliza PostgreSQL mediante Supabase.

Se crearon las tablas:
- assets.
- work_orders.

Las órdenes se relacionan con los activos mediante la clave foránea asset_id.

Se configuraron migraciones con Alembic.

## 5. Frontend

Se desarrolló la interfaz gráfica con React y Vite.

Incluye:
- Panel principal.
- Listado y registro de activos.
- Edición y desactivación de activos.
- Registro de órdenes de trabajo.
- Consulta de órdenes.
- Actualización de estados.
- Mensajes de validación y errores.
- Comunicación con el backend mediante Axios.

## 6. Integración

Se conectó el frontend con la API mediante Axios y se configuró CORS para permitir la comunicación entre ambos componentes.

La información se almacena en PostgreSQL.

## 7. Seguridad y configuración

Se utilizan variables de entorno para configurar la conexión a la base de datos. Los archivos .env están excluidos del repositorio mediante .gitignore.

## 8. Verificaciones

- Se verificó la disponibilidad de los endpoints.
- Se aplicaron las migraciones de base de datos.
- Se ejecutaron pruebas automatizadas.
- Se verificó la comunicación entre frontend y backend.
- Se comprobó la persistencia de los registros.

Los resultados detallados se encuentran en las fases 4 y 5.

## 9. Resultado

Se cuenta con un backend funcional, una interfaz web desarrollada y una integración con PostgreSQL.

Las funcionalidades principales de gestión de activos y órdenes de trabajo fueron implementadas y verificadas.