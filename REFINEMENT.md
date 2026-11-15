# Ejercicio de análisis y refinamiento

## Propósito

En un proyecto real, los requerimientos no siempre contienen toda la información necesaria. Este ejercicio busca conocer cómo identificas información faltante, formulas preguntas, documentas supuestos, reconoces riesgos y priorizas.

No existe una única respuesta correcta.

## Instrucciones

Para cada escenario:

1. Escribe preguntas adicionales.
2. Registra tus supuestos.
3. Explica la decisión que implementarás.
4. Identifica riesgos.

## Escenario 1: Activos duplicados

> El sistema debe permitir registrar activos y evitar registros duplicados.

Considera preguntas como: ¿cuándo son duplicados?, ¿el nombre es único?, ¿existe serial o código externo?, ¿se consideran activos inactivos?, ¿se bloquea o solo se advierte?

### Preguntas adicionales
```text
1. ¿Se debe considerar un código interno, serial o placa de inventario físico además del nombre como criterio estricto de unicidad?
2. ¿Los activos inactivos participan en la validación de duplicados para impedir que se reingrese un equipo con el mismo nombre, tipo y ubicación bajo otro estado?
3. ¿El sistema debe rechazar por completo la inserción de un activo duplicado devolviendo un código de conflicto o permitir una advertencia interactiva al usuario?
```
### Supuestos
```text
1. Un activo es considerado duplicado si coincide exactamente en nombre (`name`), tipo (`asset_type`) y ubicación (`location`).
2. La validación debe contemplar tanto activos activos como inactivos para preservar la integridad histórica del inventario.
3. El sistema debe bloquear la operación de forma estricta y retornar un error controlado.
```
### Decisión de implementación
```text
Se validará la unicidad en la capa de servicios de FastAPI y se respaldará a nivel de base de datos con un índice único funcional en PostgreSQL denominado exactamente `uq_assets_normalized_identity`, utilizando las expresiones: `LOWER(BTRIM(name))`, `LOWER(BTRIM(asset_type))` y `LOWER(BTRIM(location))`. Cualquier intento de duplicado producirá un código HTTP `409 Conflict`.
```
### Riesgos
```text
1. Que diferencias mínimas involuntarias en la captura de datos (ej. errores tipográficos sutiles) pasen la validación y generen duplicados lógicos.
2. Que restricciones rígidas de unicidad bloqueen el registro de equipos similares en una misma área si no se incorporan atributos diferenciadores.
```

## Escenario 2: Eliminación de activos

> El usuario debe poder eliminar un activo.

Un activo puede tener órdenes asociadas. ¿Debe eliminarse permanentemente?, ¿qué ocurre con sus órdenes?, ¿es preferible desactivarlo?, ¿debe pedirse confirmación?

### Preguntas adicionales
```text
1. ¿Se requiere un mecanismo de borrado permanente o la eliminación debe ser exclusivamente lógica?
2. ¿Qué ocurre con las órdenes de trabajo históricas asociadas a un activo dado de baja?
3. ¿Los activos inactivos deben seguir apareciendo en los listados y consultas habituales de la interfaz?
```
### Supuestos
```text
1. Los activos nunca se eliminan físicamente de la base de datos (`DELETE`) para salvaguardar la integridad referencial y la trazabilidad de las órdenes.
2. La acción solicitada como eliminación corresponde en realidad a una desactivación lógica (cambio de estado a Inactivo).
3. Las órdenes de trabajo históricas deben conservarse íntegras y asociadas al activo.
```
### Decisión
```text
No se implementará borrado físico. Se utilizará un endpoint dedicado para desactivación lógica (`PATCH /api/assets/{id}/deactivate`), el cual modificará el estado del activo a Inactivo, manteniendo su disponibilidad para consultas y preservando todas sus órdenes asociadas.
```
### Riesgos
```text
1. Crecimiento acumulativo de registros inactivos obsoletos en tablas transaccionales a largo plazo.
2. Posible confusión visual en el frontend si no se diferencian claramente los equipos activos de los inactivos.
```

## Escenario 3: Órdenes simultáneas

> Se debe crear una orden de trabajo para realizar mantenimiento sobre un activo.

No se indica si un activo puede tener varias órdenes abiertas al mismo tiempo. ¿Se debe bloquear?, ¿advertir?, ¿qué estados se consideran abiertos?

### Preguntas adicionales
```text
1. ¿Puede un activo poseer múltiples órdenes de trabajo abiertas al mismo tiempo?
2. ¿Se debe restringir la creación de órdenes si el activo se encuentra inactivo?
3. ¿Cómo interactúan las prioridades de distintas órdenes sobre un mismo equipo?
```
### Supuestos
```text
1. Funcionalmente, se permite que un activo tenga múltiples órdenes de trabajo registradas y abiertas de manera simultánea (ej. una revisión eléctrica y una reparación mecánica).
2. Está prohibido crear nuevas órdenes de trabajo para activos que se encuentren en estado Inactivo.
3. Las prioridades operan de forma independiente por cada orden.
```
### Decisión
```text
Se permitirá que un activo tenga múltiples órdenes de trabajo abiertas simultáneamente, validando de forma previa que el activo exista y se encuentre en estado Activo. Si el activo está inactivo, la operación será rechazada con HTTP `409 Conflict`. A nivel técnico, la creación de órdenes y la desactivación de activos deben coordinarse mediante bloqueo de filas y transacciones atómicas seguras, utilizando `with_for_update()` cuando corresponda para evitar condiciones de carrera.
```
### Riesgos
```text
1. Saturación operativa de órdenes abiertas sobre un mismo equipo crítico sin una supervisión centralizada adecuada.
```

## Escenario 4: Flujo de estados

> Las órdenes pueden estar pendientes, en progreso o finalizadas.

Considera: ¿se puede finalizar directamente una pendiente?, ¿puede reabrirse?, ¿hace falta `Cancelada`?, ¿deben registrarse fechas de inicio/finalización?

### Preguntas adicionales
```
1. ¿Se permite saltar el estado intermedio pasando directamente de Pendiente a Finalizada?
2. ¿Una orden finalizada puede ser reabierta o modificada en su estado?
3. ¿Se requiere un estado adicional como Cancelada en el MVP?
```
### Supuestos
```
1. El ciclo de vida de una orden es estrictamente secuencial y unidireccional: Pendiente → En progreso → Finalizada.
2. No se permiten saltos de estado ni retrocesos de ningún tipo.
3. No se contempla el estado Cancelada ni la reversión de órdenes finalizadas en el alcance actual.
```
### Decisión
```
Se implementará una máquina de estados rígida en la capa de servicios del backend que valide exclusivamente las transiciones permitidas (Pendiente a En progreso, y En progreso a Finalizada). Cualquier salto o intento de modificar una orden finalizada provocará un error HTTP `409 Conflict`.
```
### Riesgos
```text
1. Falta de flexibilidad ante errores operativos humanos al registrar cambios de estado definitivos.
```

## Escenario 5: Priorización

> Las órdenes pueden tener prioridad baja, media o alta.

No se indica quién asigna la prioridad ni qué efecto tiene. ¿Se puede cambiar?, ¿alta aparece primero?, ¿requiere justificación?

### Preguntas adicionales
```
1. ¿Quién define la prioridad al momento de registrar la orden?
2. ¿La prioridad influye en la ejecución automática o solo en la visualización?
3. ¿Es obligatoria la edición posterior de la prioridad?
```
### Supuestos
```
1. La prioridad debe ser seleccionada obligatoriamente por el usuario al momento de crear una orden de trabajo.
2. Los valores permitidos son acotados estrictamente a Baja, Media y Alta. Pydantic validará que se proporcione una prioridad válida sin establecer valores predeterminados automáticos.
3. Su función principal en el MVP es ordenar visualmente la atención técnica mediante componentes gráficos distintivos.
```
### Decisión
```
Se requerirá el campo `priority` como obligatorio en la carga útil de creación, validando que contenga alguno de los valores permitidos (Baja, Media, Alta), sin incorporar reglas de prioridad automática, y permitiendo su visualización mediante etiquetas tipográficas en el listado de la interfaz.
```
### Riesgos
```
1. Asignación masiva y subjetiva de prioridad Alta a todas las órdenes, perdiendo efectividad operativa.
```

## Escenario 6: Responsables

> Las órdenes deben ser atendidas por personal de mantenimiento.

La versión obligatoria no solicita gestión de usuarios o cuadrillas. ¿Debe incluir responsable?, ¿uno o varios?, ¿forma parte de esta versión?

### Preguntas adicionales
```text
1. ¿Se requiere un módulo de usuarios, perfiles o autenticación para asignar responsables?
2. ¿La gestión de cuadrillas forma parte del alcance obligatorio del MVP?
```
### Supuestos
```text
1. La autenticación de usuarios, roles y gestión de cuadrillas quedan completamente fuera del alcance obligatorio del MVP.
2. Las órdenes se gestionan asociadas directamente a los activos y sus descripciones técnicas globales.
```
### Decisión
```text
Se omitirá la asignación de responsables y la autenticación de usuarios en esta versión, enfocando los esfuerzos en la solidez del inventario y el ciclo de vida de las órdenes.
```
### Riesgos
```text
1. Ausencia de trazabilidad individual sobre el personal técnico que ejecuta físicamente el mantenimiento.
```

# Priorización

Clasifica cada funcionalidad como Obligatoria, Importante, Opcional o Fuera del alcance.

| Funcionalidad | Clasificación | Justificación |
|---|---|---|
| Registrar activos | Obligatoria | Requisito base fundamental para construir el inventario físico y técnico. |
| Listar activos | Obligatoria | Permite consultar el estado operativo general de la infraestructura. |
| Editar activos | Obligatoria | Necesario para corregir metadatos manteniendo la identidad y el identificador del equipo. |
| Desactivar activos | Obligatoria | Sustituye el borrado físico para preservar la integridad referencial histórica. |
| Crear órdenes | Obligatoria | Inicia las acciones correctivas o preventivas sobre equipos existentes. |
| Consultar órdenes | Obligatoria | Permite dar seguimiento al estado técnico de las solicitudes de mantenimiento. |
| Cambiar estado | Obligatoria | Controla el flujo unidireccional y estricto del ciclo de vida de las tareas. |
| Autenticación | Fuera del alcance | No contemplada en las especificaciones del núcleo operativo inicial. |
| Dashboard | Opcional | Previsto para fases posteriores orientadas a analítica gerencial y KPIs. |
| Docker | Opcional | Facilita la portabilidad pero no bloquea la ejecución y validación local. |
| Notificaciones | Fuera del alcance | Excluido del alcance básico de la prueba técnica. |
| Aplicación móvil | Fuera del alcance | El diseño web responsive cubre las necesidades de visualización actuales. |
| Gestión de cuadrillas | Fuera del alcance | Fuera del alcance funcional acordado para el MVP. |
| Historial | Opcional | Útil para auditorías avanzadas posteriores a la entrega del núcleo. |
| Exportación Excel | Fuera del alcance | Funcionalidad complementaria no solicitada en los requerimientos core. |
| Despliegue en nube | Opcional | Dependiente de la infraestructura disponible para demostración pública. |

# Diseño de la solución

## Tecnologías y motivo
```text
- Backend: Python con FastAPI por su tipado estricto, Pydantic v2, alto rendimiento y documentación interactiva automática (Swagger).
- ORM: SQLAlchemy 2.0 para un manejo relacional robusto, tipado y seguro.
- Migraciones: Alembic para el control de versiones del esquema de base de datos.
- Frontend: React con Vite y React Router para una SPA moderna, rápida y modular.
- Base de datos: PostgreSQL alojada en Supabase para persistencia relacional en la nube.
- Pruebas: Pytest para la validación automatizada de reglas de negocio y componentes.
```
## Organización del código
```text
Arquitectura monolítica modular organizada por capas estrictas:

- `core/`
- `models/`
- `schemas/`
- `repositories/`
- `services/`
- `routers/`
- `exceptions/`
- `tests/`

Ubicada bajo la carpeta `backend/app/`, y complementada por `frontend/src/` y la documentación en `docs/`.
```
## Persistencia
```text
PostgreSQL en Supabase, utilizando conexiones seguras con SSL (`sslmode=require`), manejadores de sesión transaccionales y marcas de tiempo con zona horaria (`TIMESTAMP WITH TIME ZONE` y `DateTime(timezone=True)`).
```
## Validaciones
```text
Validación robusta en doble capa: Pydantic v2 en las entradas HTTP (tipos, longitudes y enumeraciones estrictas) y lógica de negocio en la capa de servicios para unicidad, relaciones y reglas de transición.
```
## Manejo de errores
```text
Estructura de errores centralizada y uniforme basada en excepciones personalizadas (`AppException`) y manejadores globales de FastAPI que gestionan las excepciones personalizadas, errores HTTP, errores de validación de Pydantic y errores internos inesperados sin exponer trazas de código ni información sensible. Las respuestas devuelven una estructura uniforme:

json
{
  "message": "El activo ya existe.",
  "code": 409,
  "error": "DUPLICATE_ASSET",
  "details": []
}



Donde:

- `message` contiene la descripción del error.
- `code` contiene el código HTTP numérico.
- `error` identifica el tipo de error.
- `details` contiene información adicional cuando corresponda.

```
## Pruebas prioritarias
```text
Suite automatizada con Pytest enfocada en validar reglas de negocio críticas, restricciones de unicidad mediante índices funcionales en PostgreSQL (`uq_assets_normalized_identity`), control de concurrencia (`with_for_update()`), transiciones de estados e integridad referencial. Las pruebas de integración se ejecutarán contra una instancia real de PostgreSQL una vez finalizado el desarrollo de las fases correspondientes.

```
## Riesgos de seguridad identificados
```text
Exposición accidental de credenciales o cadenas de conexión (mitigado mediante el uso riguroso de variables de entorno y exclusión en `.gitignore`) y ausencia inicial de autenticación o roles de usuario (gestionado como limitación documentada del MVP).
```

# Plan de trabajo

| Paso | Actividad | Resultado esperado |
|---|---|---|
| 1 | Análisis y refinamiento | REFINEMENT.md consolidado y estructurado |
| 2 | Diseño técnico | Arquitectura y modelos definidos |
| 3 | Preparación del entorno | Estructura de directorios y configuración del entorno preparadas para su ejecución local |
| 4 | Desarrollo del backend | Modelos, esquemas, repositorios y servicios implementados |
| 5 | Configuración e integración con Supabase | Conexión a PostgreSQL y migraciones Alembic ejecutadas |
| 6 | Desarrollo del frontend | Vistas, componentes, formularios y servicios Axios implementados |
| 7 | Integración y pruebas | Pruebas unitarias y de integración ejecutadas con Pytest |
| 8 | Documentación y preparación de la sustentación | README.md y guías técnicas preparadas |
| 9 | Funcionalidades opcionales | Componentes post-MVP evaluados o incorporados |

# Resultado final

## Funcionalidades completadas
```text

```
## Funcionalidades pendientes
```text

```
## Principal dificultad encontrada
```text

```
## ¿Cómo resolviste los problemas encontrados?
```text

```
## ¿Qué mejorarías con más tiempo?
```text

```
## Tiempo aproximado dedicado
```text

```
## ¿Utilizaste herramientas de inteligencia artificial? ¿Para qué?
```text

```
## ¿Qué parte del código consideras más importante explicar?
```text

```

# Conocimientos sobre Microsoft 365 y Copilot

Como parte de la prueba técnica, responde las siguientes preguntas relacionadas con Microsoft 365, Copilot Studio y el desarrollo de aplicaciones basadas en agentes.

---

## 1. Microsoft 365 y Copilot

### ¿Qué es Microsoft 365 y qué recursos interoperan con Copilot?

### Respuesta

```text
Microsoft 365 es una plataforma de productividad basada en la nube que integra aplicaciones de ofimática, colaboración y gestión corporativa (Word, Excel, PowerPoint, Outlook, Teams, SharePoint, OneDrive). Copilot actúa como un asistente de inteligencia artificial generativa integrado de manera transversal en estas herramientas. Los recursos que interoperan directamente con Copilot incluyen documentos de texto, libros de cálculo, sitios y listas estructuradas en SharePoint, bandejas de correo en Outlook, así como transcripciones y chats en Teams, todo orquestado de forma segura a través de la API de Microsoft Graph.
```

---

## 2. Copilot Studio

### ¿Qué es Copilot Studio y qué ofrece?

### Respuesta

```text
Copilot Studio es una herramienta de desarrollo integral de bajo código (low-code) diseñada para crear, personalizar y gestionar agentes conversacionales de inteligencia artificial (copilots) adaptados a procesos de negocio específicos. Ofrece capacidades para conectar bases de conocimientos externas, integrar APIs empresariales mediante conectores personalizados, definir flujos de diálogo avanzados, aplicar restricciones de seguridad y directrices operativas (`guardrails`), y supervisar mediante analíticas el rendimiento de las interacciones.
```

---

## 3. Aplicaciones basadas en agentes

### ¿Qué mejores prácticas consideras para implementar, comprobar y evaluar aplicaciones con agentes?

### Respuesta

```text
1. Fundamentación sólida (Grounding): Conectar el agente estrictamente a fuentes de datos verificadas y controladas (RAG) para minimizar las alucinaciones.
2. Delimitación de alcance (Guardrails): Establecer instrucciones de sistema claras sobre qué dominios maneja el agente y cómo debe rechazar consultas fuera de su competencia.
3. Validación y pruebas continuas: Implementar conjuntos de datos de prueba (`eval sets`) con preguntas estándar y casos límite para medir la precisión y relevancia de las respuestas.
4. Monitoreo y retroalimentación: Revisar de forma periódica los registros de conversación para detectar fallas de comprensión, ambigüedades o vacíos de conocimiento.
```

---

## 4. Caso práctico: aplicación de inventario

> **Esta pregunta tiene un peso especial dentro de la evaluación.**

### Describa un caso de uso e implementación para una aplicación de inventario con información en varios archivos bajo el ambiente Microsoft 365 y Copilot.

### Respuesta


- **Caso de uso:** Una empresa de mantenimiento industrial distribuye su inventario de activos y el registro de sus órdenes de trabajo entre Listas de SharePoint y libros de Excel compartidos en OneDrive.
```
- Implementación:
  - Almacenamiento: Las tablas maestras de activos se alojan en Listas de SharePoint para garantizar control de versiones, auditoría y concurrencia, mientras que los reportes operativos dinámicos se estructuran en archivos de Excel en OneDrive.
  - Permisos y Seguridad: Se administran mediante Microsoft Entra ID (anteriormente Azure Active Directory) aplicando el principio de mínimo privilegio por roles.
  - Conectores y Recuperación: Un agente creado en Copilot Studio utiliza conectores de Microsoft Graph y flujos de Power Automate para consultar la información almacenada en SharePoint y OneDrive, de acuerdo con los permisos configurados y los esquemas de integración establecidos.
  - Acciones y Validación: Las solicitudes de modificación o creación enviadas a través del chat pueden ser interpretadas y canalizadas mediante flujos de Power Automate que aplican validaciones de negocio antes de confirmar la escritura en los repositorios de datos.
  - Evaluación: Se audita periódicamente la precisión del agente comparando las respuestas devueltas frente a consultas de control ejecutadas sobre el inventario real.
```
