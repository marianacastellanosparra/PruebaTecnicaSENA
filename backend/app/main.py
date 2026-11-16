from fastapi import FastAPI

app = FastAPI(
    title="ORION Maintenance Lite",
    description="API para la gestión de activos y órdenes de trabajo.",
    version="0.1.0",
)


@app.get("/api/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "application": "ORION Maintenance Lite",
    }