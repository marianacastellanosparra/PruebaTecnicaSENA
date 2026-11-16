# ORION Maintenance Lite

# Fase 3: Preparación del entorno de desarrollo

## 1. Descripción de la fase

Durante esta fase se realizó la preparación del entorno de desarrollo de **ORION Maintenance Lite**, dejando configuradas las herramientas, dependencias y estructuras iniciales necesarias para comenzar la implementación del sistema.

El trabajo se desarrolló tomando como referencia las decisiones establecidas en las fases anteriores:

- `REFINEMENT.md`: documento de análisis y refinamiento de requerimientos.
- `docs/fase-02-diseno-tecnico/DISENO_TECNICO.md`: documento de diseño técnico y arquitectura del sistema.

El propósito fue disponer de una estructura organizada para trabajar de manera independiente en el backend y el frontend, manteniendo la arquitectura aprobada y evitando implementar funcionalidades antes de la fase correspondiente.

## 2. Entorno de desarrollo utilizado

Para preparar el entorno se utilizaron las siguientes herramientas:

| Herramienta | Utilización en el proyecto |
|---|---|
| Python | Entorno de desarrollo del backend. |
| FastAPI | Framework seleccionado para construir la API REST. |
| SQLAlchemy 2.0 | ORM previsto para la comunicación con PostgreSQL. |
| Pydantic 2 | Validación y estructuración de datos. |
| Alembic | Preparación del sistema de migraciones. |
| PostgreSQL / Supabase | Motor de base de datos definido para el proyecto. |
| React | Desarrollo de la interfaz de usuario. |
| Vite | Creación y ejecución del entorno frontend. |
| React Router | Organización de la navegación. |
| Axios | Comunicación HTTP con el backend. |
| Pytest | Framework seleccionado para las pruebas automatizadas. |
| Git | Control de versiones del proyecto. |
| GitHub | Repositorio remoto para almacenar el código fuente. |

### 2.1. Versiones del entorno

Se realizó la comprobación de las herramientas instaladas en el equipo mediante los comandos correspondientes.

| Herramienta | Comando utilizado | Versión obtenida |
|---|---|---|
| Python | `py --version` | Python 3.14.3 |
| Node.js | `node --version` | v24.13.1 |
| npm | `npm --version` | 11.8.0 |
| Git | `git --version` | git version 2.53.0.windows.1 |

## 3. Organización del repositorio

Se preparó la estructura de trabajo del proyecto para mantener separados los componentes del backend, el frontend y la documentación.

La organización general contempla:

```text
ORION-MAINTENANCE-LITE/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── routers/
│   │   └── exceptions/
│   │
│   ├── tests/
│   │   ├── unit/
│   │   └── integration/
│   │
│   ├── alembic/
│   ├── alembic.ini
│   ├── requirements.txt
│   ├── pytest.ini
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── styles/
│   │
│   ├── index.html
│   ├── package.json
│   └── .env.example
│
├── docs/
│   ├── fase-02-diseno-tecnico/
│   │   └── DISENO_TECNICO.md
│   └── ...
│
├── .gitignore
├── REFINEMENT.md
└── README.md
```

La estructura representa la organización prevista para el desarrollo. Los directorios se irán completando con sus respectivos archivos durante las fases de implementación.

## 4. Preparación del backend

Se preparó el entorno de Python destinado al desarrollo de la API de ORION Maintenance Lite.

### 4.1. Entorno virtual

Se creó un entorno virtual independiente dentro del directorio `backend`, con el propósito de aislar las dependencias del proyecto y evitar conflictos con otros proyectos de Python instalados en el equipo.

La ubicación definida fue:

```text
backend/.venv/
```

### 4.2. Dependencias

Se creó el archivo `backend/requirements.txt` para centralizar las dependencias necesarias para el desarrollo del backend.

Se incorporaron las siguientes librerías:

| Dependencia | Función |
|---|---|
| fastapi | Construcción de la API REST. |
| uvicorn | Servidor ASGI para ejecutar FastAPI. |
| sqlalchemy | Gestión de modelos y operaciones de base de datos. |
| pydantic | Validación de datos. |
| pydantic-settings | Administración de configuraciones. |
| python-dotenv | Lectura de variables de entorno. |
| alembic | Control de migraciones. |
| psycopg2-binary | Conector de PostgreSQL. |
| pytest | Ejecución de pruebas automatizadas. |
| httpx | Cliente HTTP para pruebas de endpoints. |

Las versiones se restringieron mediante rangos compatibles para mantener un entorno controlado.

### 4.3. Aplicación inicial

Se preparó `backend/app/main.py` con una instancia inicial de FastAPI.

También se incorporó el endpoint:

```text
GET /api/health
```

Este endpoint permite comprobar posteriormente que la aplicación puede iniciar y responder solicitudes HTTP.

Su implementación es únicamente una comprobación técnica del entorno y no representa todavía una funcionalidad de negocio.

### 4.4. Configuración de pruebas

Se creó `backend/pytest.ini` para establecer la ubicación y los patrones de identificación de las futuras pruebas automatizadas.

Se prepararon los directorios:

- `backend/tests/unit/`
- `backend/tests/integration/`

Las pruebas de las reglas de negocio y de las operaciones con PostgreSQL se desarrollarán en las fases posteriores.

### 4.5. Configuración de variables de entorno

Se creó `backend/.env.example` como plantilla de configuración.

Se contemplaron las variables necesarias para el entorno de desarrollo, incluyendo:

- `ENVIRONMENT`
- `DATABASE_URL`
- `FRONTEND_ORIGIN`

No se incorporaron credenciales reales al repositorio. La conexión efectiva con Supabase se configurará en la fase correspondiente.

## 5. Preparación de Alembic

Se inicializó la estructura de Alembic dentro del backend para dejar preparado el sistema de control de migraciones de la base de datos.

La estructura generada contempla:

```text
backend/
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
└── alembic.ini
```

Durante esta fase únicamente se preparó la estructura de migraciones.

No se generaron migraciones de las tablas de activos y órdenes de trabajo, debido a que los modelos SQLAlchemy y su metadata corresponden a la implementación posterior del backend.

## 6. Preparación del frontend

Se creó el proyecto frontend utilizando React y Vite, estableciendo un entorno independiente para el desarrollo de la interfaz de usuario.

### 6.1. Dependencias

Se instalaron las dependencias iniciales:

| Dependencia | Utilización |
|---|---|
| React | Construcción de la interfaz. |
| React DOM | Renderizado de la aplicación. |
| Vite | Servidor de desarrollo y compilación. |
| React Router DOM | Administración de rutas. |
| Axios | Comunicación con la API. |

### 6.2. Organización inicial

Se preparó la estructura de `frontend/src` para organizar posteriormente los componentes, páginas, rutas, servicios, hooks y estilos de la aplicación.

### 6.3. Variables de entorno

Se creó `frontend/.env.example` con la variable:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

Esta variable permitirá establecer la dirección base del backend desde el frontend cuando se realice la integración.

## 7. Control de versiones y protección de archivos

Se preparó el archivo `.gitignore` en la raíz del repositorio para excluir archivos generados durante el desarrollo y evitar la publicación de información privada.

Se contemplaron exclusiones para:

- Entornos virtuales de Python.
- Dependencias instaladas de Node.js.
- Archivos temporales de Python.
- Caché y resultados temporales de pruebas.
- Archivos de compilación de Vite.
- Variables de entorno locales.
- Archivos propios de editores y sistemas operativos.

Se mantuvieron permitidos los archivos `.env.example`, ya que contienen únicamente plantillas sin credenciales reales.

También se preparó el repositorio Git para registrar los avances del proyecto mediante commits.

## 8. Verificaciones realizadas

En esta sección se documentan las comprobaciones realizadas durante la preparación del entorno.

| Elemento comprobado | Resultado |
|---|---|
| Versiones de Python, Node.js, npm y Git | Pendiente de registrar |
| Creación del entorno virtual | Pendiente de registrar |
| Instalación de dependencias del backend | Pendiente de registrar |
| Importación de la aplicación FastAPI | Pendiente de registrar |
| Inicio del servidor backend | Pendiente de registrar |
| Respuesta de `/api/health` | Pendiente de registrar |
| Acceso a Swagger | Pendiente de registrar |
| Instalación de dependencias frontend | Pendiente de registrar |
| Inicio del servidor Vite | Pendiente de registrar |
| Inicialización de Alembic | Pendiente de registrar |
| Configuración de Git | Pendiente de registrar |
| Creación del commit | Pendiente de registrar |
| Publicación en GitHub | Pendiente de registrar |

Los resultados se actualizarán a medida que se realicen las verificaciones. No se consideran exitosas las actividades que todavía no hayan sido ejecutadas.

## 9. Evidencias del desarrollo

Las evidencias de esta fase estarán relacionadas con los archivos y resultados obtenidos durante la preparación del entorno.

Se contemplan las siguientes evidencias:

1. Versiones de las herramientas instaladas.
2. Estructura de directorios del proyecto.
3. Archivo `requirements.txt` y dependencias instaladas.
4. Aplicación inicial de FastAPI.
5. Endpoint de salud y documentación Swagger.
6. Archivos de configuración de Alembic.
7. Proyecto React con Vite y dependencias instaladas.
8. Archivos `.env.example`.
9. Archivo `.gitignore`.
10. Historial de commits y repositorio remoto en GitHub.

Las capturas y resultados correspondientes se incorporarán conforme se complete cada actividad.

## 10. Alcance de la preparación

Al terminar esta fase se busca dejar disponible la infraestructura inicial necesaria para comenzar la implementación de ORION Maintenance Lite.

Por lo tanto, esta etapa no contempla todavía:

- Implementación de los modelos de activos y órdenes de trabajo.
- Esquemas de validación de negocio.
- Repositorios y servicios.
- Endpoints funcionales de activos y órdenes.
- Reglas de transición de estados.
- Manejo centralizado de excepciones.
- Migración inicial de la base de datos.
- Integración real con Supabase.
- Desarrollo de la interfaz funcional.
- Pruebas de las reglas de negocio.

Estas actividades se desarrollarán en las fases correspondientes, respetando el diseño técnico aprobado.

## 11. Resultado de la fase

La Fase 3 tiene como finalidad dejar organizado y configurado el entorno de desarrollo de ORION Maintenance Lite.

El resultado se documentará a partir de las actividades efectivamente realizadas, las configuraciones incorporadas al repositorio y las verificaciones obtenidas.

Con esta preparación se establece la base de trabajo para continuar con la implementación del backend, la integración con PostgreSQL y el desarrollo del frontend.