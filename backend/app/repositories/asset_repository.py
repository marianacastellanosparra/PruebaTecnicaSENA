from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import AssetCreate


def create_asset(db: Session, asset_data: AssetCreate) -> Asset:
    new_asset = Asset(**asset_data.model_dump())
    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)
    return new_asset


def get_all_assets(db: Session):
    return db.query(Asset).order_by(Asset.id).all()


def get_asset_by_id(db: Session, asset_id: int):
    return db.query(Asset).filter(Asset.id == asset_id).first()


def update_asset(db: Session, asset: Asset, asset_data: AssetCreate):
    for field, value in asset_data.model_dump().items():
        setattr(asset, field, value)

    db.commit()
    db.refresh(asset)
    return asset

def deactivate_asset(db: Session, asset: Asset):
    asset.status = "Inactivo"
    db.commit()
    db.refresh(asset)
    return asset