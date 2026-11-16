from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.exceptions.asset_exceptions import DuplicateAssetError
from app.models.asset import Asset
from app.repositories.asset_repository import (
    create_asset,
    get_all_assets,
    get_asset_by_id,
    update_asset,
    deactivate_asset,
)
from app.schemas.asset import AssetCreate


# HU-01: Registrar un activo
def register_asset(db: Session, asset_data: AssetCreate):
    existing = db.query(Asset).filter(
        func.lower(func.btrim(Asset.name)) == asset_data.name.lower(),
        func.lower(func.btrim(Asset.asset_type)) == asset_data.asset_type.lower(),
        func.lower(func.btrim(Asset.location)) == asset_data.location.lower()
    ).first()

    if existing:
        raise DuplicateAssetError("El activo ya existe.")

    try:
        return create_asset(db, asset_data)
    except IntegrityError:
        db.rollback()
        raise DuplicateAssetError("El activo ya existe.")


# HU-02: Consultar todos los activos
def list_assets(db: Session):
    return get_all_assets(db)


# HU-02: Consultar un activo por ID
def find_asset(db: Session, asset_id: int):
    return get_asset_by_id(db, asset_id)


# HU-03: Editar un activo
def edit_asset(db: Session, asset_id: int, asset_data: AssetCreate):
    asset = get_asset_by_id(db, asset_id)

    if not asset:
        return None

    duplicate = db.query(Asset).filter(
        Asset.id != asset_id,
        func.lower(func.btrim(Asset.name)) == asset_data.name.lower(),
        func.lower(func.btrim(Asset.asset_type)) == asset_data.asset_type.lower(),
        func.lower(func.btrim(Asset.location)) == asset_data.location.lower()
    ).first()

    if duplicate:
        raise DuplicateAssetError("Ya existe otro activo con esos datos.")

    try:
        return update_asset(db, asset, asset_data)
    except IntegrityError:
        db.rollback()
        raise DuplicateAssetError("Ya existe otro activo con esos datos.")


# HU-04: Desactivar un activo
def disable_asset(db: Session, asset_id: int):
    asset = get_asset_by_id(db, asset_id)

    if not asset:
        return None

    return deactivate_asset(db, asset)