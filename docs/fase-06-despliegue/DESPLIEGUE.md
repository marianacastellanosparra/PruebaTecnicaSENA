
# Fase 6: Despliegue y ejecución de ORION Maintenance Lite

## 1. Objetivo

Documentar el procedimiento para activar el backend y frontend de ORION Maintenance Lite y visualizar la aplicación web en un navegador.

En esta fase se describe la ejecución local del proyecto. No se realizó un despliegue público en un servidor externo.

## 2. Requisitos previos

Antes de ejecutar el proyecto se necesita:

- Python instalado.
- Node.js y npm instalados.
- Git instalado.
- Repositorio del proyecto descargado.
- Base de datos PostgreSQL configurada.
- Archivo `.env` configurado en la carpeta `backend`.
- Dependencias del backend y frontend instaladas.

## 3. Activar el backend

El backend está desarrollado con Python y FastAPI.

### Paso 1. Abrir Git Bash

Ingresar a la carpeta del backend:

```bash
cd ~/PruebaTecnicaSENA/backend
```

### Paso 2. Activar el entorno virtual

```bash
source .venv/Scripts/activate
```

### Paso 3. Ejecutar las migraciones

```bash
python -m alembic upgrade head
```

Este comando actualiza la estructura de la base de datos.

### Paso 4. Iniciar el servidor

```bash
uvicorn app.main:app --reload
```

El backend queda disponible en:

```text
http://127.0.0.1:8000
```

Documentación de la API:

```text
http://127.0.0.1:8000/docs
```

Comprobación del estado:

```text
http://127.0.0.1:8000/api/health
```

## 4. Activar el frontend

El frontend está desarrollado con React y Vite.

### Paso 1. Abrir una segunda terminal

Mantener abierta la terminal del backend y abrir otra ventana de Git Bash.

Ingresar a la carpeta del frontend:

```bash
cd ~/PruebaTecnicaSENA/frontend
```

### Paso 2. Instalar dependencias

```bash
npm install
```

Este paso se realiza cuando sea necesario instalar o actualizar las dependencias del proyecto.

### Paso 3. Iniciar el servidor de desarrollo

```bash
npm run dev
```

El frontend queda disponible en:

```text
http://localhost:5173/
```

## 5. Visualizar la aplicación

Abrir Google Chrome o cualquier navegador e ingresar a:

```text
http://localhost:5173/
```

Desde la interfaz se pueden realizar las siguientes operaciones:

- Registrar activos.
- Consultar activos.
- Editar activos.
- Desactivar y reactivar activos.
- Crear órdenes de trabajo.
- Consultar órdenes de trabajo.
- Cambiar el estado de las órdenes.

## 6. Verificación del funcionamiento

Para comprobar que la aplicación funciona correctamente se realizan las siguientes verificaciones:

1. Confirmar que el backend esté ejecutándose.
2. Ingresar a `/api/health` y comprobar la respuesta de la API.
3. Abrir la documentación en `/docs`.
4. Confirmar que el frontend cargue correctamente.
5. Registrar un activo desde la interfaz.
6. Crear una orden de trabajo asociada al activo.
7. Cambiar el estado de la orden.
8. Actualizar la página y comprobar que los datos permanezcan guardados.

## 7. Solución de problemas comunes

| Problema | Posible solución |
|---|---|
| No se encuentra el módulo de la aplicación | Verificar que se está ejecutando el comando desde la carpeta `backend`. |
| No se activa el entorno virtual | Comprobar que exista la carpeta `.venv`. |
| Error de conexión con PostgreSQL | Revisar la variable `DATABASE_URL` del archivo `.env`. |
| El frontend no carga | Verificar que se ejecutó `npm run dev`. |
| Error de comunicación con la API | Revisar la URL de `VITE_API_BASE_URL` y la configuración CORS. |
| El puerto está ocupado | Cerrar el proceso que utiliza el puerto o configurar otro puerto disponible. |

## 8. Consideraciones

- Se deben mantener abiertas las dos terminales mientras se utiliza la aplicación.
- La terminal del backend ejecuta FastAPI.
- La terminal del frontend ejecuta React con Vite.
- Los archivos `.env` contienen configuraciones privadas y no deben subirse a GitHub.
- La ejecución documentada corresponde a un entorno local.
- El despliegue público queda como una posible mejora futura.

## 9. Resultado de la fase

Se documentó el procedimiento para iniciar los servicios del backend y frontend, conectarlos con la base de datos PostgreSQL y visualizar ORION Maintenance Lite desde un navegador.

La aplicación puede ejecutarse localmente mediante:

- Backend: `http://127.0.0.1:8000`
- Frontend: `http://localhost:5173/`
- Documentación API: `http://127.0.0.1:8000/docs`

**Estado:** Ejecución local documentada. No se realizó despliegue público.
