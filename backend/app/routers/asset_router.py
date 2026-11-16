from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.exceptions.asset_exceptions import DuplicateAssetError
from app.schemas.asset import AssetCreate, AssetResponse
from app.services.asset_service import (
    register_asset,
    list_assets,
    find_asset,
    edit_asset,
    disable_asset,
)

router = APIRouter(prefix="/api/assets", tags=["Assets"])


# HU-01: Registrar un activo
@router.post("", response_model=AssetResponse, status_code=201)
def create_new_asset(
    asset_data: AssetCreate,
    db: Session = Depends(get_db)
):
    try:
        return register_asset(db, asset_data)
    except DuplicateAssetError as error:
        raise HTTPException(status_code=409, detail=str(error))


# HU-02: Consultar todos los activos
@router.get("", response_model=list[AssetResponse])
def get_assets(db: Session = Depends(get_db)):
    return list_assets(db)


# HU-02: Consultar un activo por ID
@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(
    asset_id: int,
    db: Session = Depends(get_db)
):
    asset = find_asset(db, asset_id)

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Activo no encontrado"
        )

    return asset


# HU-03: Editar un activo
@router.put("/{asset_id}", response_model=AssetResponse)
def update_existing_asset(
    asset_id: int,
    asset_data: AssetCreate,
    db: Session = Depends(get_db)
):
    try:
        asset = edit_asset(db, asset_id, asset_data)

        if not asset:
            raise HTTPException(
                status_code=404,
                detail="Activo no encontrado"
            )

        return asset

    except DuplicateAssetError as error:
        raise HTTPException(status_code=409, detail=str(error))


# HU-04: Desactivar un activo
@router.patch("/{asset_id}/deactivate", response_model=AssetResponse)
def deactivate_existing_asset(
    asset_id: int,
    db: Session = Depends(get_db)
):
    asset = disable_asset(db, asset_id)

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Activo no encontrado"
        )

    return asset