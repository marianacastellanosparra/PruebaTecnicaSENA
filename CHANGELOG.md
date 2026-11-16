
# CHANGELOG - ORION Maintenance Lite

Este archivo registra cronológicamente la planeación, organización, desarrollo, integración, pruebas y documentación del proyecto ORION Maintenance Lite, realizado como parte de la prueba técnica para aprendices y practicantes SENA.

---

## [Planeación inicial] - 2026-11-14

### 1. Organización de la prueba técnica

- Revisión de las instrucciones y requisitos de la prueba técnica ORION Maintenance Lite.
- Análisis del objetivo principal y alcance del proyecto.
- Identificación de las funcionalidades obligatorias y opcionales.
- Organización de las actividades necesarias para desarrollar la solución.
- Definición de las etapas de trabajo.
- Planeación de la estructura general del repositorio.
- Identificación de los documentos y entregables solicitados.
- Organización inicial de las historias de usuario.
- Planeación del backlog de actividades.
- Identificación de las tecnologías necesarias para el desarrollo.
- Organización del tiempo disponible para realizar la prueba técnica.
- Preparación del plan de trabajo para iniciar el desarrollo.

---

## [1.0.0] - 2026-11-15

### 2. Análisis y refinamiento de requerimientos

- Revisión detallada de los requerimientos establecidos en la prueba técnica.
- Identificación del problema relacionado con la gestión y mantenimiento de activos.
- Definición del alcance funcional de la aplicación.
- Identificación de las necesidades del sistema.
- Organización de las historias de usuario.
- Elaboración y actualización del archivo `REFINEMENT.md`.
- Priorización de funcionalidades mediante el backlog.
- Identificación de reglas de negocio y criterios de aceptación.
- Identificación de riesgos y posibles mejoras futuras.

### 3. Diseño técnico

- Definición de la arquitectura general del sistema.
- Separación de la aplicación en frontend y backend.
- Selección de tecnologías y herramientas de desarrollo.
- Definición de la estructura de la base de datos.
- Diseño de las entidades Activos y Órdenes de trabajo.
- Definición de las relaciones entre las entidades.
- Establecimiento de las reglas para el manejo de estados y prioridades.
- Documentación de las decisiones técnicas en `DISENO_TECNICO.md`.

### 4. Preparación del entorno de desarrollo

- Creación de la estructura de carpetas del proyecto.
- Configuración del entorno virtual de Python.
- Preparación de las dependencias del backend.
- Configuración inicial del proyecto frontend con React y Vite.
- Configuración de las variables de entorno.
- Configuración de Git y GitHub para el control de versiones.
- Configuración del archivo `.gitignore`.
- Preparación de la conexión con PostgreSQL.

### 5. Desarrollo del backend

- Implementación de la API REST utilizando FastAPI.
- Configuración de SQLAlchemy para la conexión y gestión de la base de datos.
- Configuración de Pydantic para la validación de datos.
- Organización del backend mediante modelos, esquemas, repositorios, servicios y routers.
- Implementación de la gestión de activos.
- Implementación de la gestión de órdenes de trabajo.
- Creación de excepciones para el manejo de errores.
- Configuración de Alembic para las migraciones de la base de datos.
- Creación de las tablas `assets` y `work_orders`.
- Configuración de la relación entre activos y órdenes de trabajo mediante clave foránea.
- Implementación del endpoint para verificar el estado de la API.

### 6. Gestión de activos

- Implementación del registro de activos.
- Validación de los campos obligatorios: nombre, tipo y ubicación.
- Asignación automática de identificador y fecha de registro.
- Asignación del estado inicial Activo.
- Implementación de consulta y listado de activos.
- Implementación de consulta individual por identificador.
- Implementación de edición de información.
- Implementación de desactivación de activos.
- Conservación de los registros desactivados, evitando su eliminación física.
- Validación de registros inexistentes y datos incorrectos.

### 7. Gestión de órdenes de trabajo

- Implementación del registro de órdenes de trabajo.
- Asociación de cada orden con un activo existente.
- Validación de los campos obligatorios.
- Definición de prioridades Baja, Media y Alta.
- Asignación automática del identificador y fecha de creación.
- Asignación del estado inicial Pendiente.
- Implementación de consulta y listado de órdenes.
- Implementación de consulta individual por identificador.
- Implementación de transiciones de estado:
  - Pendiente a En progreso.
  - En progreso a Finalizada.
- Validación del flujo permitido de estados.
- Restricción de cambios que incumplan las reglas del proceso.

### 8. Desarrollo del frontend

- Configuración de la aplicación con React y Vite.
- Implementación de la estructura visual de la aplicación.
- Creación del menú lateral de navegación.
- Desarrollo de la vista principal.
- Implementación de la interfaz para registrar activos.
- Implementación del listado de activos.
- Incorporación de acciones para editar y desactivar activos.
- Implementación de formularios para crear órdenes de trabajo.
- Desarrollo del listado de órdenes de trabajo.
- Incorporación de acciones para cambiar el estado de las órdenes.
- Implementación de indicadores visuales para los estados.
- Incorporación de mensajes de validación y manejo de errores.
- Adaptación de la interfaz para diferentes tamaños de pantalla.

### 9. Integración del sistema

- Integración del frontend con el backend mediante Axios.
- Configuración de la URL base de la API mediante variables de entorno.
- Configuración de CORS para permitir la comunicación entre frontend y backend.
- Integración de las operaciones de activos.
- Integración de las operaciones de órdenes de trabajo.
- Verificación de la comunicación con PostgreSQL.
- Validación de la persistencia de los registros.
- Comprobación del funcionamiento de los servicios desde la interfaz web.

### 10. Pruebas y validación

- Configuración de Pytest para las pruebas automatizadas.
- Implementación de pruebas unitarias para los servicios de activos.
- Implementación de pruebas unitarias para los servicios de órdenes de trabajo.
- Implementación de pruebas de integración para los endpoints de activos.
- Implementación de pruebas de integración para los endpoints de órdenes de trabajo.
- Implementación de pruebas para el endpoint de salud de la API.
- Verificación de validaciones de campos obligatorios.
- Verificación de respuestas ante registros inexistentes.
- Verificación de las reglas de transición de estados.
- Ejecución de pruebas automatizadas con resultado de 24 pruebas exitosas.
- Validación manual del registro, edición y desactivación de activos.
- Validación manual de creación y actualización de órdenes de trabajo.
- Verificación de persistencia de información después de recargar la aplicación.
- Ejecución de la compilación de producción del frontend.
- Ejecución del análisis estático del frontend, sin errores y con dos advertencias.

### 11. Documentación

- Actualización del README principal del proyecto.
- Documentación de la instalación y ejecución del backend.
- Documentación de la instalación y ejecución del frontend.
- Documentación de las tecnologías utilizadas.
- Actualización del archivo `REFINEMENT.md`.
- Organización del archivo `BACKLOG.md`.
- Documentación del desarrollo en `docs/fase-03-desarrollo/DESARROLLO.md`.
- Documentación de las pruebas en `docs/fase-04-pruebas/PLAN_PRUEBAS.md`.
- Documentación de la integración en `docs/fase-05-integracion/INTEGRACION.md`.
- Creación del archivo `CHANGELOG.md` para registrar los cambios del proyecto.

---

## 12. Funcionalidades pendientes y mejoras futuras

Las siguientes funcionalidades no están implementadas en la versión actual y se consideran posibles mejoras:

- Implementación de autenticación y autorización de usuarios.
- Administración de responsables de las órdenes de trabajo.
- Historial de cambios de las órdenes.
- Búsqueda avanzada de activos y órdenes.
- Filtros por estado, prioridad y tipo de activo.
- Panel de indicadores y estadísticas.
- Implementación de despliegue público.
- Automatización de integración y entrega continua.

---

## 13. Estado de la versión

**Proyecto:** ORION Maintenance Lite.

**Versión:** 1.0.0.

**Periodo de trabajo:** 14 y 15 de noviembre de 2026.

**Estado:** Versión funcional con gestión de activos, gestión de órdenes de trabajo, integración frontend-backend y pruebas automatizadas.

**Resultado de pruebas:** 24 pruebas exitosas.

**Tecnologías principales:** Python, FastAPI, SQLAlchemy, PostgreSQL, Alembic, React, Vite y Axios.