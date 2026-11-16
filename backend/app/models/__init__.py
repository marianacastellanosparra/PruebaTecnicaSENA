"""Modelos de base de datos de ORION Maintenance Lite."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.asset import Asset
from app.models.work_order import WorkOrder

__all__ = ["Base", "Asset", "WorkOrder"]