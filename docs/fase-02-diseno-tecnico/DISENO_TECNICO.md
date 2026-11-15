
# Definición de la Solución Técnica

Este documento establece la definición de la solución técnica para el proyecto **ORION Maintenance Lite**, detallando las tecnologías seleccionadas, la arquitectura, el diseño de la base de datos, la estructura del proyecto, la organización de los componentes y las decisiones técnicas que orientarán su implementación.

El propósito de esta fase es definir cómo se construirá la solución antes de iniciar su desarrollo, manteniendo la coherencia con los requerimientos, supuestos y decisiones documentados en la fase 1.

**Ubicación del documento:** `docs/fase-02-diseno-tecnico/DISENO_TECNICO.md`

---

## 1. Selección de Tecnologías y Herramientas

Para garantizar el cumplimiento de los requerimientos de la prueba técnica, se selecciona un conjunto de tecnologías que permita desarrollar una solución organizada, mantenible y escalable.

### 1.1. Backend

- **Python:** Lenguaje de programación principal del servidor, seleccionado por su legibilidad, facilidad de mantenimiento y amplio ecosistema para el desarrollo backend.

- **FastAPI:** Framework web de alto rendimiento para construir APIs REST, con validación de datos integrada y documentación interactiva automática mediante Swagger/OpenAPI.

- **SQLAlchemy 2.0:** ORM (Object-Relational Mapper) moderno de Python para gestionar la persistencia y el mapeo objeto-relacional de manera segura y eficiente. Se utilizará su API síncrona, en coherencia con el controlador `psycopg2-binary`.

- **Pydantic 2:** Librería de validación de esquemas y serialización de datos en tiempo de ejecución. Permitirá validar los tipos, longitudes y campos obligatorios, evitando cadenas vacías o compuestas únicamente por espacios en blanco.

- **pydantic-settings:** Librería utilizada para administrar y validar la configuración de la aplicación mediante variables de entorno, facilitando la separación entre configuración y código fuente.

- **Alembic:** Herramienta para administrar y controlar la evolución del esquema de la base de datos mediante migraciones DDL versionadas.

- **Pytest:** Framework para la automatización de pruebas unitarias y de integración sobre los componentes y servicios del backend.

### 1.2. Base de datos y persistencia

- **PostgreSQL:** Sistema de gestión de bases de datos relacional que ofrece integridad referencial, restricciones de dominio, índices funcionales y control transaccional ACID.

- **Supabase:** Plataforma en la nube utilizada para el alojamiento gestionado de la base de datos PostgreSQL del proyecto.

- **psycopg2-binary:** Controlador de PostgreSQL utilizado por SQLAlchemy para establecer la conexión con la base de datos. Las conexiones se configurarán mediante los parámetros correspondientes de la URL de conexión, incluyendo obligatoriamente `sslmode=require`.

### 1.3. Frontend

- **React:** Biblioteca de JavaScript basada en componentes para desarrollar interfaces de usuario interactivas y reutilizables.

- **Vite:** Herramienta de desarrollo y compilación frontend que proporciona recarga en caliente (HMR) y un entorno de desarrollo eficiente.

- **JavaScript:** Lenguaje utilizado para implementar la lógica del cliente.

- **React Router:** Librería para gestionar las rutas y la navegación modular dentro de la aplicación de página única (SPA).

- **Axios:** Cliente HTTP basado en promesas para consumir los endpoints de la API REST desarrollada con FastAPI.

- **CSS:** Hojas de estilo utilizadas para construir una interfaz intuitiva y adaptable a diferentes tamaños de pantalla (responsive).

### 1.4. Control de versiones

- **Git:** Herramienta de control de versiones distribuido utilizada para gestionar los cambios del código fuente mediante commits pequeños, descriptivos y progresivos.

---

## 2. Estructura y Organización del Proyecto

El proyecto se organiza mediante una separación entre documentación, backend y frontend. Esta estructura facilita el mantenimiento y permite incorporar progresivamente los entregables de cada fase.

### 2.1. Estructura actual del repositorio

La organización documental se realiza mediante directorios independientes dentro de `docs/`, correspondientes a las diferentes etapas del proyecto.

La estructura de referencia del repositorio es la siguiente:

```text
ORION-MAINTENANCE-LITE/
│
├── docs/
│   ├── fase-01-analisis/
│   ├── fase-02-diseno-tecnico/
│   │   └── DISENO_TECNICO.md
│   ├── fase-03-desarrollo/
│   ├── fase-04-pruebas/
│   ├── fase-05-integracion/
│   ├── fase-06-despliegue/
│   ├── fase-07-documentacion/
│   ├── fase-08-validacion-final/
│   └── fase-09-entrega/
│
├── backend/
├── frontend/
│
├── REFINEMENT.md
├── BACKLOG.md
├── README.md
├── CHANGELOG.md
└── .gitignore
```

Los directorios y archivos correspondientes a las siguientes fases se incorporarán progresivamente, respetando la organización por etapas.

Esta estructura representa la organización del repositorio y debe mantenerse actualizada de acuerdo con los archivos y directorios que realmente existan.

### 2.2. Estructura técnica prevista para el backend

Para el desarrollo del backend se contempla una arquitectura modular organizada por capas, con la siguiente estructura:

```text
backend/
│
├── app/
│   ├── __init__.py
│   ├── core/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── repositories/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   ├── routers/
│   │   └── __init__.py
│   ├── exceptions/
│   │   └── __init__.py
│   └── main.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── requirements.txt
├── alembic.ini
├── pytest.ini
└── .env.example
```

### 2.3. Estructura técnica prevista para el frontend

La aplicación frontend se organizará mediante componentes, páginas, rutas y servicios independientes:

```text
frontend/
│
├── index.html
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   ├── components/
│   ├── pages/
│   ├── routes/
│   ├── services/
│   ├── hooks/
│   └── styles/
│
├── package.json
├── vite.config.js
└── .env.example
```

Los archivos de ejemplo de configuración serán:

- `backend/.env.example`: documentará las variables necesarias para la configuración del backend y la conexión a PostgreSQL.
- `frontend/.env.example`: documentará las variables necesarias para configurar la URL base de la API.

Estos archivos no contendrán credenciales reales, contraseñas ni claves privadas. Los archivos `.env` utilizados localmente deberán estar excluidos del control de versiones mediante `.gitignore`.

La estructura anterior representa una referencia de organización técnica. No implica que deban crearse anticipadamente archivos vacíos o carpetas sin utilidad. Cada elemento se incorporará cuando corresponda a su fase de implementación.

---

## 3. Modelo de Datos

### 3.1. Modelo de datos relacional

El esquema de base de datos estará compuesto por dos tablas principales: `assets` y `work_orders`.

Ambas estarán relacionadas mediante una clave foránea, garantizando la integridad referencial y la conservación del historial de mantenimiento.

### Tabla: `assets` (Activos)

| Campo | Tipo de dato | Restricciones / Reglas | Descripción |
|---|---|---|---|
| `id` | INTEGER | PK, autoincremental | Identificador único del activo |
| `name` | VARCHAR(100) | NOT NULL | Nombre del activo |
| `asset_type` | VARCHAR(50) | NOT NULL | Tipo de activo |
| `location` | VARCHAR(150) | NOT NULL | Ubicación física |
| `status` | VARCHAR(20) | NOT NULL, DEFAULT 'Activo' | Estado operativo del activo |
| `created_at` | TIMESTAMP WITH TIME ZONE | NOT NULL, DEFAULT NOW() | Fecha y hora de creación generada por el sistema |

Los campos `name`, `asset_type` y `location` son obligatorios y no pueden contener cadenas vacías ni valores compuestos únicamente por espacios en blanco.

**Índice único funcional: `uq_assets_normalized_identity`**

Para evitar registros duplicados considerando la combinación de nombre, tipo y ubicación, se define un índice único funcional en PostgreSQL.

La comparación ignora las diferencias entre mayúsculas y minúsculas y los espacios al inicio y al final de los valores.

La restricción aplica tanto a activos activos como inactivos.

```sql
CREATE UNIQUE INDEX uq_assets_normalized_identity
ON assets (
    LOWER(BTRIM(name)),
    LOWER(BTRIM(asset_type)),
    LOWER(BTRIM(location))
);
```

**Restricciones CHECK de activos**

Se establecen las siguientes restricciones para garantizar la integridad de los datos:

```sql
CHECK (status IN ('Activo', 'Inactivo')),
CHECK (name ~ '[^[:space:]]'),
CHECK (asset_type ~ '[^[:space:]]'),
CHECK (location ~ '[^[:space:]]')
```

Estas restricciones garantizan que el estado corresponda a uno de los valores permitidos y que los campos obligatorios contengan al menos un carácter que no sea espacio en blanco.

La validación se complementa con los esquemas Pydantic y las reglas de negocio del backend.

### Tabla: `work_orders` (Órdenes de Trabajo)

| Campo | Tipo de dato | Restricciones / Reglas | Descripción |
|---|---|---|---|
| `id` | INTEGER | PK, autoincremental | Identificador único de la orden |
| `asset_id` | INTEGER | FK (`assets.id`), NOT NULL | Identificador del activo relacionado |
| `title` | VARCHAR(120) | NOT NULL | Título de la orden |
| `description` | TEXT | NOT NULL | Descripción detallada del trabajo |
| `priority` | VARCHAR(20) | NOT NULL, sin valor predeterminado | Prioridad de la orden |
| `status` | VARCHAR(20) | NOT NULL, DEFAULT 'Pendiente' | Estado de la orden |
| `created_at` | TIMESTAMP WITH TIME ZONE | NOT NULL, DEFAULT NOW() | Fecha y hora de creación generada por el sistema |

Los campos `title` y `description` son obligatorios y no pueden contener cadenas vacías ni valores compuestos únicamente por espacios en blanco.

La prioridad debe ser seleccionada obligatoriamente por el usuario y solamente admite los valores `Baja`, `Media` y `Alta`.

El estado inicial de cada orden se asigna automáticamente como `Pendiente`.

**Restricciones CHECK de órdenes**

```sql
CHECK (priority IN ('Baja', 'Media', 'Alta')),
CHECK (status IN ('Pendiente', 'En progreso', 'Finalizada')),
CHECK (title ~ '[^[:space:]]'),
CHECK (description ~ '[^[:space:]]')
```

Estas restricciones permiten controlar los valores admitidos para prioridad y estado, además de impedir que los campos de texto obligatorios contengan únicamente espacios en blanco.

Las restricciones CHECK no garantizan por sí solas la secuencia lógica de transición de estados. Esta regla se validará en la capa de servicios.

### 3.2. Relaciones e integridad referencial

**Cardinalidad 1:N**

Un activo puede tener asociadas múltiples órdenes de trabajo. Cada orden de trabajo pertenece exactamente a un único activo.

Se permite que un mismo activo posea varias órdenes abiertas simultáneamente, con prioridades independientes.

**Integridad referencial**

La clave foránea `work_orders.asset_id` se configurará con la restricción `ON DELETE RESTRICT`.

Esto impide eliminar físicamente un activo que tenga órdenes de trabajo asociadas, protegiendo la integridad referencial y conservando el historial técnico.

**Desactivación lógica**

Los activos no se eliminan físicamente desde la aplicación.

La eliminación solicitada funcionalmente se implementará mediante desactivación lógica, utilizando el endpoint:

```http
PATCH /api/assets/{id}/deactivate
```

Esta operación cambiará el estado del activo a `Inactivo`, conservando sus órdenes históricas.

Los activos inactivos no podrán recibir nuevas órdenes de trabajo. Cualquier intento de crear una orden sobre uno de ellos será rechazado con HTTP `409 Conflict`.

---

## 4. Organización de los Componentes

### 4.1. Capas del backend (FastAPI)

Se implementará una arquitectura monolítica modular con separación de responsabilidades.

La organización propuesta contempla las siguientes capas:

- **core/:** Configuración global de la aplicación mediante `pydantic-settings`, conexión al motor SQLAlchemy y gestión de sesiones de base de datos.

- **models/:** Definición de las clases ORM que representan las entidades y relaciones del modelo de datos.

- **schemas/:** Esquemas Pydantic 2 utilizados para validar los datos de entrada y serializar las respuestas de la API.

- **repositories/:** Capa de acceso a datos encargada de interactuar con SQLAlchemy para realizar consultas y operaciones CRUD.

- **services/:** Capa de lógica de negocio responsable de aplicar las reglas de validación de unicidad, restricciones de activos inactivos, máquina de estados y control transaccional.

- **routers/:** Controladores REST de FastAPI que exponen los endpoints HTTP y gestionan las solicitudes y respuestas de la API.

- **exceptions/:** Manejo centralizado de excepciones personalizadas (`AppException`) y manejadores globales de FastAPI para estandarizar las respuestas de error sin exponer trazas internas ni información sensible.

La estructura permitirá mantener separadas las responsabilidades de acceso a datos, lógica de negocio y comunicación HTTP.

### 4.2. Capas del frontend (React SPA)

El frontend se organizará mediante componentes reutilizables y módulos independientes:

- **components/:** Elementos visuales reutilizables, como barras de navegación, insignias de estado, formularios y modales.

- **pages/:** Vistas principales de la aplicación, como listados de activos, formularios de creación y vistas de órdenes de trabajo.

- **routes/:** Configuración centralizada de las rutas mediante React Router.

- **services/:** Módulos basados en Axios para la comunicación asíncrona con los endpoints del backend.

- **hooks/:** Funciones reutilizables para gestionar lógica de estado y operaciones asíncronas.

- **styles/:** Hojas de estilo CSS organizadas para mantener una interfaz consistente y adaptable.

### 4.3. Validación de campos de texto obligatorios

Para garantizar la calidad de los datos, se utilizará una estrategia de validación en dos niveles.

**Validación mediante Pydantic 2**

Los esquemas validarán los campos obligatorios de activos y órdenes de trabajo, evitando:

- Cadenas vacías (`""`).
- Cadenas compuestas únicamente por espacios en blanco.
- Campos obligatorios ausentes en la petición.
- Valores que no correspondan al tipo de dato esperado.
- Valores que superen las longitudes máximas establecidas.

**Validación mediante PostgreSQL**

La base de datos complementará las validaciones de entrada mediante:

- Restricciones CHECK.
- Claves primarias y foráneas.
- Índice único funcional `uq_assets_normalized_identity`.
- Restricciones de dominio para estados y prioridades.

De esta manera, la integridad de los datos estará protegida tanto en la entrada de la API como directamente en la base de datos.

### 4.4. Máquina de estados de las órdenes de trabajo

El ciclo de vida de una orden de trabajo seguirá estrictamente la siguiente secuencia:

```text
Pendiente → En progreso → Finalizada
```

**Reglas de transición**

Las transiciones serán validadas en la capa de servicios:

1. Toda orden nueva se creará automáticamente en estado `Pendiente`.
2. Se permitirá pasar de `Pendiente` a `En progreso`.
3. Se permitirá pasar de `En progreso` a `Finalizada`.
4. No se permitirán saltos de estado, como pasar directamente de `Pendiente` a `Finalizada`.
5. No se permitirán retrocesos, como regresar de `En progreso` a `Pendiente`.
6. Una orden que alcance el estado `Finalizada` no podrá cambiar nuevamente su estado.

No se contempla el estado `Cancelada` dentro del alcance del MVP.

Cualquier intento de realizar una transición no permitida generará una respuesta HTTP `409 Conflict`.

La máquina de estados permite mantener un ciclo de vida controlado y evitar modificaciones inconsistentes en las órdenes de trabajo.

### 4.5. Control de concurrencia y transacciones atómicas (`with_for_update()`)

Para proteger la integridad del sistema y evitar condiciones de carrera (*race conditions*) ante solicitudes simultáneas, se utilizará bloqueo pesimista mediante `with_for_update()` de SQLAlchemy, coordinado con transacciones atómicas en PostgreSQL.

**Creación de órdenes de trabajo**

1. Iniciar una transacción.
2. Obtener el bloqueo de la fila del activo mediante `with_for_update()`.
3. Comprobar que el activo existe.
4. Verificar que el activo se encuentra en estado `Activo`.
5. Crear la orden de trabajo.
6. Confirmar la transacción mediante `COMMIT`.

**Desactivación de activos**

1. Iniciar una transacción.
2. Bloquear la fila del activo utilizando `with_for_update()`.
3. Verificar que el activo existe.
4. Cambiar su estado a `Inactivo`.
5. Confirmar la transacción mediante `COMMIT`.

**Cambio de estado de órdenes**

1. Iniciar una transacción.
2. Bloquear la fila de la orden mediante `with_for_update()`.
3. Comprobar el estado actual.
4. Validar la transición permitida según la máquina de estados.
5. Guardar el nuevo estado.
6. Confirmar la transacción mediante `COMMIT`.

**Coordinación de bloqueos**

La creación de órdenes y la desactivación de activos deberán bloquear exactamente la misma fila del activo mediante `with_for_update()`, manteniendo el bloqueo hasta que finalice la transacción.

Esto permite coordinar ambas operaciones:

- Si la creación de la orden obtiene primero el bloqueo, la desactivación deberá esperar hasta que finalice la transacción.
- Si la desactivación obtiene primero el bloqueo, la creación deberá esperar y posteriormente comprobar nuevamente que el activo continúe en estado `Activo`.

De esta manera se evita registrar nuevas órdenes sobre activos que ya fueron desactivados.

**Manejo de errores transaccionales**

Las operaciones se ejecutarán dentro de transacciones explícitas.

Cuando una operación finalice correctamente, se ejecutará `COMMIT` para confirmar los cambios.

Ante cualquier excepción durante una operación transaccional, se ejecutará `ROLLBACK` para revertir los cambios realizados y evitar estados parciales en la base de datos.

---

## 5. Decisiones Técnicas y Justificación

### 5.1. Justificación de FastAPI

Se selecciona FastAPI por su rendimiento, su integración con Pydantic y la generación automática de documentación interactiva mediante Swagger/OpenAPI.

Estas características facilitan la validación de datos, la exposición de endpoints REST y las pruebas de los servicios.

### 5.2. Justificación de React y Vite

React permite desarrollar una interfaz basada en componentes reutilizables, facilitando la separación de las vistas y la lógica de presentación.

Vite proporciona un entorno de desarrollo eficiente y recarga en caliente (HMR), agilizando el proceso de construcción del frontend.

### 5.3. Justificación de PostgreSQL y Supabase

PostgreSQL ofrece integridad relacional, transacciones ACID, restricciones CHECK, claves foráneas e índices funcionales.

Estas características son necesarias para implementar las reglas de unicidad de activos y proteger las relaciones entre activos y órdenes de trabajo.

Supabase proporciona alojamiento gestionado para la base de datos PostgreSQL, facilitando su disponibilidad y administración.

### 5.4. Justificación de SQLAlchemy y Alembic

SQLAlchemy 2.0 permite gestionar la persistencia mediante un ORM moderno, facilitando las consultas y operaciones sobre las entidades del sistema.

Alembic permite administrar los cambios del esquema mediante migraciones versionadas, manteniendo un historial controlado de la evolución de la base de datos.

### 5.5. Justificación de Pydantic y pydantic-settings

Pydantic permite validar los tipos, formatos, longitudes y restricciones de los datos recibidos por la API.

pydantic-settings facilita la administración de la configuración mediante variables de entorno, evitando incluir credenciales y configuraciones sensibles directamente en el código fuente.

### 5.6. Justificación de Pytest

Pytest permite automatizar las pruebas unitarias y de integración, facilitando la verificación de las reglas de negocio, el comportamiento de los servicios y la interacción con la base de datos.

### 5.7. Justificación de la arquitectura monolítica modular

Se selecciona una arquitectura monolítica modular porque permite organizar el sistema mediante componentes y capas independientes, sin incorporar la complejidad operativa de los microservicios.

La separación entre frontend y backend es organizativa y estructural. No implica que el sistema esté compuesto por microservicios.

Esta decisión permite mantener una solución sencilla, organizada y adecuada al alcance funcional del MVP.

### 5.8. Estrategia de pruebas automatizadas

La estrategia de pruebas se define en esta fase como parte del diseño técnico. Su implementación y ejecución se realizarán durante las etapas posteriores del proyecto.

Se utilizará Pytest para desarrollar pruebas unitarias y de integración.

**Pruebas unitarias**

Se podrán utilizar dependencias simuladas o datos aislados para comprobar de manera independiente la lógica de negocio, las validaciones y el comportamiento de los servicios.

**Pruebas de integración**

Se utilizará una instancia real de PostgreSQL para validar el comportamiento conjunto de los componentes y las reglas críticas de persistencia.

Se deberán comprobar especialmente:

- Restricciones CHECK de las tablas.
- Índice único funcional `uq_assets_normalized_identity`.
- Claves foráneas.
- Restricción `ON DELETE RESTRICT`.
- Transacciones y operaciones de bloqueo mediante `FOR UPDATE`.
- Comportamiento ante solicitudes concurrentes.

**Consideración técnica sobre PostgreSQL y SQLite**

SQLite no debe considerarse un sustituto equivalente de PostgreSQL para validar el comportamiento de los bloqueos de fila mediante `FOR UPDATE`, debido a que ambos motores gestionan la concurrencia de manera diferente.

Por este motivo, las pruebas que requieran comprobar el comportamiento real de los bloqueos y las transacciones deberán ejecutarse contra PostgreSQL.

---

## 6. Alcance de la Solución Técnica

El diseño técnico se mantiene alineado con las funcionalidades obligatorias y las decisiones establecidas en la fase 1.

La solución contempla:

- Registro, consulta y edición de activos.
- Desactivación lógica de activos.
- Prevención de activos duplicados.
- Creación y consulta de órdenes de trabajo.
- Asociación de órdenes con activos.
- Gestión de prioridades Baja, Media y Alta.
- Control del ciclo de vida de las órdenes de trabajo.
- Validaciones de datos en backend y base de datos.
- Manejo uniforme de errores.
- Protección de operaciones simultáneas mediante transacciones y bloqueos.

Se mantienen fuera del alcance obligatorio del MVP:

- Autenticación y gestión de usuarios.
- Roles y permisos.
- Asignación de responsables y gestión de cuadrillas.
- Notificaciones.
- Aplicación móvil.
- Exportación a Excel.
- Dashboard y funcionalidades avanzadas de analítica.
- Otras funcionalidades opcionales no contempladas en los requerimientos obligatorios.

Las funcionalidades opcionales podrán evaluarse en etapas posteriores, siempre que no afecten el cumplimiento del alcance principal.

---

## 7. Resultado de la Definición Técnica

Con esta fase se establece la base técnica para iniciar la implementación de ORION Maintenance Lite.

Se han definido:

- Las tecnologías y herramientas que se utilizarán.
- La estructura prevista del backend y frontend.
- El modelo relacional de la base de datos.
- Las relaciones y restricciones de integridad.
- La organización de los componentes y las responsabilidades de cada capa.
- Las reglas de validación de datos.
- La máquina de estados de las órdenes de trabajo.
- La estrategia de concurrencia y manejo de transacciones.
- Las decisiones técnicas y su justificación.
- La estrategia de pruebas automatizadas.

El diseño mantiene la coherencia con los escenarios, supuestos, decisiones y prioridades documentados en la fase 1.

Por lo tanto, la solución cuenta con una definición técnica que servirá como referencia para las siguientes etapas de preparación del entorno, desarrollo del backend, configuración de la base de datos, desarrollo del frontend e integración.

La implementación de los componentes y la ejecución de las pruebas se realizarán en sus respectivas fases, siguiendo las decisiones establecidas en este documento.
