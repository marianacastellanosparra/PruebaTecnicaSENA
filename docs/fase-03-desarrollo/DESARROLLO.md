
# ORION Maintenance Lite
# Fase 3: Desarrollo

## 1. Descripción de la fase

En esta fase se realizó el desarrollo de los componentes principales del proyecto ORION Maintenance Lite, teniendo como objetivo construir una API para gestionar activos y órdenes de trabajo de mantenimiento.

Se implementó la estructura del backend, la conexión con la base de datos, los modelos, las operaciones de consulta y modificación, las reglas de negocio y los endpoints necesarios para cumplir con las funcionalidades principales.

El frontend desarrollado con React y Vite se encuentra pendiente de implementación.

## 2. Tecnologías y herramientas utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes tecnologías:

### Backend
- Python 3.14.3.
- FastAPI para la construcción de la API REST.
- SQLAlchemy para la interacción con la base de datos.
- Pydantic para la validación de datos.
- Alembic para el control de migraciones.
- PostgreSQL como sistema de gestión de base de datos.
- Supabase como servicio de base de datos.
- Pytest para las pruebas automatizadas.

### Frontend
- React.
- Vite.
- React Router DOM.
- Axios.

**Estado:** pendiente de desarrollo e integración con el backend.

### Control de versiones
- Git.
- GitHub.

## 3. Organización del proyecto

El repositorio se organizó separando el backend, el frontend y la documentación.

La estructura principal es la siguiente:

```text
PruebaTecnicaSENA/
│
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── config/
│   │   ├── exceptions/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── services/
│   ├── tests/
│   │   ├── unit/
│   │   └── integration/
│   ├── .env.example
│   ├── .gitignore
│   └── requirements.txt
│
├── frontend/
│
└── docs/
    ├── fase-02-diseno-tecnico/
    ├── fase-03-desarrollo/
    └── fase-04-pruebas/
```

## 4. Desarrollo del backend

Se implementó el backend utilizando FastAPI, organizando el código por responsabilidades para facilitar su mantenimiento y comprensión.

La aplicación cuenta con los siguientes componentes:

### 4.1 Modelos

Se crearon los modelos correspondientes a las entidades principales del sistema:

- **Asset:** representa los activos que se registran para su mantenimiento.
- **WorkOrder:** representa las órdenes de trabajo asociadas a los activos.

Los modelos se relacionan mediante una relación de uno a muchos: un activo puede tener varias órdenes de trabajo.

### 4.2 Esquemas de validación

Se utilizaron esquemas de Pydantic para validar la información recibida y definir la estructura de los datos que entrega la API.

Se incluyen validaciones para los campos obligatorios, valores permitidos y formatos de información.

### 4.3 Repositorios

Se implementaron repositorios para separar las operaciones de acceso a la base de datos de la lógica del sistema.

Entre sus responsabilidades se encuentran:

- Registrar activos.
- Consultar activos.
- Actualizar activos.
- Desactivar activos.
- Registrar órdenes de trabajo.
- Consultar órdenes de trabajo.
- Consultar órdenes para actualizar su estado.

### 4.4 Servicios

Se desarrollaron servicios para implementar las reglas de negocio del proyecto.

Entre las principales reglas implementadas están:

- Evitar el registro de activos duplicados.
- Validar que los activos existan antes de crear órdenes de trabajo.
- Impedir la creación de órdenes para activos inactivos.
- Permitir la desactivación de activos sin eliminar sus registros.
- Controlar las transiciones de estado de las órdenes de trabajo.
- Impedir cambios de estado que no sigan el flujo establecido.

### 4.5 Endpoints de la API

Se implementaron los siguientes endpoints:

| Método | Endpoint | Funcionalidad |
|---|---|---|
| GET | `/api/health` | Verificar el estado de la API. |
| POST | `/api/assets` | Registrar un activo. |
| GET | `/api/assets` | Consultar todos los activos. |
| GET | `/api/assets/{asset_id}` | Consultar un activo por ID. |
| PUT | `/api/assets/{asset_id}` | Actualizar un activo. |
| PATCH | `/api/assets/{asset_id}/deactivate` | Desactivar un activo. |
| POST | `/api/work-orders` | Crear una orden de trabajo. |
| GET | `/api/work-orders` | Consultar todas las órdenes. |
| GET | `/api/work-orders/{work_order_id}` | Consultar una orden por ID. |
| PATCH | `/api/work-orders/{work_order_id}/status` | Actualizar el estado de una orden. |

## 5. Base de datos

Se configuró la conexión del backend con PostgreSQL mediante Supabase.

Se implementaron las tablas principales:

- **assets:** almacena la información de los activos.
- **work_orders:** almacena las órdenes de trabajo y su relación con los activos.

También se configuraron las claves primarias, claves foráneas, restricciones de validación e índices necesarios para mantener la integridad de los datos.

La relación entre las tablas permite asociar varias órdenes de trabajo a un mismo activo.

## 6. Migraciones con Alembic

Se configuró Alembic para administrar los cambios en la estructura de la base de datos.

Se generó y aplicó la migración:

`ddf7a5112708_create_assets_and_work_orders_tables.py`

La migración permitió crear las tablas `assets` y `work_orders`, junto con sus restricciones y relaciones.

Se verificó que la migración quedara aplicada correctamente en la base de datos.

## 7. Configuración y seguridad

Se configuraron las variables de entorno para manejar la conexión a la base de datos sin incluir credenciales directamente en el código.

Se utilizaron archivos `.env` y `.env.example` para separar la configuración local de la información que puede compartirse en el repositorio.

También se configuró `.gitignore` para evitar subir archivos sensibles y carpetas del entorno virtual.

## 8. Desarrollo del frontend

El frontend del proyecto está pendiente de desarrollo.

Se tiene previsto utilizar React y Vite para construir la interfaz gráfica y Axios para realizar las solicitudes HTTP al backend.

Entre las funcionalidades que se deberán implementar se encuentran:

- Visualización de los activos registrados.
- Registro y edición de activos.
- Consulta y desactivación de activos.
- Creación de órdenes de trabajo.
- Consulta de órdenes de trabajo.
- Actualización del estado de las órdenes.
- Integración con los endpoints del backend.

Estas funcionalidades se desarrollarán en una etapa posterior.

## 9. Verificaciones del desarrollo

Durante el desarrollo se realizaron verificaciones para comprobar la configuración y el funcionamiento del backend.

Se verificó:

- La importación de la aplicación FastAPI.
- La disponibilidad de los endpoints registrados.
- La conexión con PostgreSQL.
- La aplicación de las migraciones de Alembic.
- La ejecución de las pruebas automatizadas.

La ejecución de las pruebas se documenta con mayor detalle en el documento de la Fase 4: `docs/fase-04-pruebas/PLAN_PRUEBAS.md`.

## 10. Resultado de la fase

Como resultado de esta fase se cuenta con un backend funcional para la gestión de activos y órdenes de trabajo de mantenimiento.

Se implementaron los modelos, esquemas, repositorios, servicios, reglas de negocio, endpoints y conexión con la base de datos PostgreSQL.

El backend cuenta con pruebas unitarias y de integración documentadas en la siguiente fase.

El frontend con React y Vite permanece pendiente de desarrollo, por lo que todavía no se cuenta con una interfaz gráfica integrada con la API.

Con esto se deja preparada la base funcional del sistema para continuar con la construcción del frontend y su posterior integración.
