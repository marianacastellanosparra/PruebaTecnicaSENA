from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal
from app.models.asset import Asset


client = TestClient(app)


# HU-01: Registrar un activo y detectar duplicados
def test_create_asset_and_detect_duplicate():
    asset_name = f"Activo prueba {uuid4().hex[:8]}"

    data = {
        "name": asset_name,
        "asset_type": "Computador",
        "location": "Oficina de pruebas"
    }

    try:
        response = client.post("/api/assets", json=data)

        assert response.status_code == 201

        result = response.json()

        assert result["name"] == asset_name
        assert result["asset_type"] == "Computador"
        assert result["location"] == "Oficina de pruebas"
        assert result["status"] == "Activo"
        assert result["id"] is not None

        duplicate_response = client.post("/api/assets", json=data)

        assert duplicate_response.status_code == 409

    finally:
        db = SessionLocal()
        try:
            db.query(Asset).filter(
                Asset.name == asset_name
            ).delete(synchronize_session=False)
            db.commit()
        finally:
            db.close()


# HU-01: Validar campos obligatorios
def test_create_asset_with_empty_name():
    data = {
        "name": "   ",
        "asset_type": "Computador",
        "location": "Oficina"
    }

    response = client.post("/api/assets", json=data)

    assert response.status_code == 422


# HU-04: Desactivar un activo
def test_deactivate_asset():
    asset_name = f"Activo desactivacion {uuid4().hex[:8]}"

    data = {
        "name": asset_name,
        "asset_type": "Computador",
        "location": "Oficina de pruebas"
    }

    asset_id = None

    try:
        response = client.post("/api/assets", json=data)

        assert response.status_code == 201

        asset_id = response.json()["id"]

        response = client.patch(
            f"/api/assets/{asset_id}/deactivate"
        )

        assert response.status_code == 200
        assert response.json()["status"] == "Inactivo"

        detail = client.get(f"/api/assets/{asset_id}")

        assert detail.status_code == 200
        assert detail.json()["status"] == "Inactivo"

    finally:
        if asset_id is not None:
            db = SessionLocal()
            try:
                db.query(Asset).filter(
                    Asset.id == asset_id
                ).delete(synchronize_session=False)
                db.commit()
            finally:
                db.close()