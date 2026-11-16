from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers.asset_router import router as asset_router
from app.routers.work_order_router import router as work_order_router


app = FastAPI(
    title="ORION Maintenance Lite",
    description="API para la gestión de activos y órdenes de trabajo.",
    version="0.1.0",
)


# Configuración CORS para permitir la comunicación con React
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_ORIGIN,
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Registrar las rutas de la API
app.include_router(asset_router)
app.include_router(work_order_router)


# Endpoint para verificar el estado de la API
@app.get("/api/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "application": "ORION Maintenance Lite"
    }