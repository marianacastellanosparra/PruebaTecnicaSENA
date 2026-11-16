from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal
from app.models.asset import Asset
from app.models.work_order import WorkOrder


client = TestClient(app)


def create_test_asset():
    data = {
        "name": f"Activo orden {uuid4().hex[:8]}",
        "asset_type": "Computador",
        "location": "Oficina de pruebas"
    }

    response = client.post("/api/assets", json=data)

    assert response.status_code == 201

    return response.json()["id"]


# HU-05, HU-06 y HU-07: Flujo completo de una orden
def test_work_order_complete_flow():
    asset_id = create_test_asset()
    work_order_id = None

    data = {
        "asset_id": asset_id,
        "title": "Mantenimiento preventivo",
        "description": "Revisión general del equipo",
        "priority": "Alta"
    }

    try:
        # Crear orden
        response = client.post("/api/work-orders", json=data)

        assert response.status_code == 201

        result = response.json()
        work_order_id = result["id"]

        assert result["title"] == data["title"]
        assert result["priority"] == "Alta"
        assert result["status"] == "Pendiente"
        assert result["asset"]["id"] == asset_id

        # Consultar todas las órdenes
        response = client.get("/api/work-orders")

        assert response.status_code == 200
        assert any(
            order["id"] == work_order_id
            for order in response.json()
        )

        # Consultar una orden
        response = client.get(
            f"/api/work-orders/{work_order_id}"
        )

        assert response.status_code == 200
        assert response.json()["id"] == work_order_id

        # Intentar saltar directamente a Finalizada
        response = client.patch(
            f"/api/work-orders/{work_order_id}/status",
            json={"status": "Finalizada"}
        )

        assert response.status_code == 409

        # Cambiar a En progreso
        response = client.patch(
            f"/api/work-orders/{work_order_id}/status",
            json={"status": "En progreso"}
        )

        assert response.status_code == 200
        assert response.json()["status"] == "En progreso"

        # Cambiar a Finalizada
        response = client.patch(
            f"/api/work-orders/{work_order_id}/status",
            json={"status": "Finalizada"}
        )

        assert response.status_code == 200
        assert response.json()["status"] == "Finalizada"

    finally:
        db = SessionLocal()

        try:
            if work_order_id is not None:
                db.query(WorkOrder).filter(
                    WorkOrder.id == work_order_id
                ).delete(synchronize_session=False)

            db.query(Asset).filter(
                Asset.id == asset_id
            ).delete(synchronize_session=False)

            db.commit()

        finally:
            db.close()


# HU-05: No permitir órdenes para activos inactivos
def test_cannot_create_work_order_for_inactive_asset():
    asset_id = create_test_asset()

    try:
        response = client.patch(
            f"/api/assets/{asset_id}/deactivate"
        )

        assert response.status_code == 200
        assert response.json()["status"] == "Inactivo"

        data = {
            "asset_id": asset_id,
            "title": "Reparación",
            "description": "Revisión del equipo",
            "priority": "Media"
        }

        response = client.post("/api/work-orders", json=data)

        assert response.status_code == 409

    finally:
        db = SessionLocal()

        try:
            db.query(Asset).filter(
                Asset.id == asset_id
            ).delete(synchronize_session=False)

            db.commit()

        finally:
            db.close()