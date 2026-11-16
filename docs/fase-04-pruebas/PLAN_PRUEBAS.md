
# Plan de Pruebas – ORION Maintenance Lite

## 1. Objetivo

Verificar el funcionamiento de la API ORION Maintenance Lite mediante pruebas automatizadas, validando los servicios, endpoints, operaciones de activos, gestión de órdenes de trabajo y reglas de negocio establecidas.

## 2. Entorno de pruebas

- Lenguaje: Python 3.14.3.
- Framework: FastAPI.
- Herramienta de pruebas: Pytest 8.4.2.
- Cliente de pruebas: TestClient.
- Base de datos: PostgreSQL.
- ORM: SQLAlchemy 2.0.
- Migraciones: Alembic.
- Simulación de dependencias: unittest.mock y MagicMock.

## 3. Tipos de pruebas realizadas

### 3.1. Pruebas unitarias

Se desarrollaron 18 pruebas unitarias utilizando mocks para comprobar el comportamiento individual de los servicios sin depender de una conexión real a la base de datos.

Se verificaron las siguientes funcionalidades:

- Registro de activos.
- Detección de activos duplicados.
- Consulta de activos.
- Edición de activos.
- Desactivación de activos.
- Registro de órdenes de trabajo.
- Validación de existencia de activos.
- Restricción de órdenes para activos inactivos.
- Consulta de órdenes de trabajo.
- Transiciones permitidas de estados.
- Rechazo de transiciones no permitidas.

**Resultado: 18 pruebas aprobadas.**

### 3.2. Pruebas de integración

Se ejecutaron 6 pruebas para comprobar el funcionamiento conjunto de los componentes de la aplicación.

| ID | Prueba | Resultado |
|---|---|---|
| PT-001 | Verificar endpoint GET `/api/health` | APROBADA |
| PT-002 | Registrar un activo y detectar duplicados | APROBADA |
| PT-003 | Validar el registro de activos con nombre vacío | APROBADA |
| PT-004 | Desactivar un activo | APROBADA |
| PT-005 | Crear, consultar y actualizar órdenes de trabajo, validando sus transiciones | APROBADA |
| PT-006 | Impedir la creación de órdenes para activos inactivos | APROBADA |

**Resultado: 6 pruebas aprobadas.**

## 4. Evidencia de ejecución

### 4.1. Ejecución de pruebas unitarias

Comando utilizado:

```bash
python -m pytest tests/unit -v
```

Resultado:

```text
18 passed in 2.70s
```

### 4.2. Ejecución de todas las pruebas

Comando utilizado:

```bash
python -m pytest -v
```

Resultado:

```text
collected 24 items

24 passed, 1 warning in 14.21s
```

## 5. Observaciones

Durante la ejecución se presentó una advertencia de compatibilidad relacionada con Starlette y HTTPX.

La advertencia no afectó la ejecución ni los resultados de las pruebas.

Todas las pruebas finalizaron correctamente.

## 6. Mejoras y pruebas futuras

- Ampliar las pruebas de validación de datos.
- Probar individualmente todos los códigos de respuesta de los endpoints.
- Realizar pruebas de concurrencia en la actualización de estados de órdenes.
- Incorporar pruebas adicionales para filtros y búsquedas cuando estas funcionalidades se desarrollen.

## 7. Resultado general

El backend de ORION Maintenance Lite cuenta con pruebas unitarias y de integración aprobadas.

| Tipo | Aprobadas |
|---|---:|
| Unitarias | 18 |
| Integración | 6 |
| **Total** | **24** |

**Estado final: 24 de 24 pruebas aprobadas.**
