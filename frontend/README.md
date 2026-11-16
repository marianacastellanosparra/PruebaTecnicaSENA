# ORION Maintenance Lite - Frontend

## 1. Descripción

Interfaz web para la gestión de activos y órdenes de trabajo de ORION Maintenance Lite.

Permite registrar, consultar, editar y desactivar activos, así como crear órdenes de trabajo y gestionar sus estados.

## 2. Tecnologías utilizadas

- React 19
- Vite
- JavaScript
- Axios
- React Router DOM
- CSS

## 3. Requisitos

- Node.js
- npm
- Backend de ORION Maintenance Lite en ejecución.

## 4. Instalación

Desde la carpeta frontend, ejecutar:

```bash
npm install
```

## 5. Configuración

Crear un archivo `.env` en la carpeta frontend con:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

## 6. Ejecución

Iniciar el servidor de desarrollo:

```bash
npm run dev
```

Abrir en el navegador:

http://localhost:5173/

## 7. Compilación

Para generar la versión de producción:

```bash
npm run build
```

## 8. Verificación de código

Ejecutar:

```bash
npm run lint
```

## 9. Funcionalidades

### Gestión de activos

- Registrar activos.
- Consultar activos.
- Editar información.
- Desactivar activos.

### Gestión de órdenes de trabajo

- Crear órdenes.
- Consultar órdenes.
- Asociar órdenes con activos.
- Gestionar prioridades.
- Cambiar estados: Pendiente, En progreso y Finalizada.

## 10. Conexión con el backend

El frontend consume los servicios REST desarrollados con FastAPI mediante Axios.

URL base:

http://127.0.0.1:8000/api