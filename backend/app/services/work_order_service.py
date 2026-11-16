from sqlalchemy.orm import Session

from app.exceptions.work_order_exceptions import (
    AssetNotFoundError,
    InactiveAssetError,
    InvalidWorkOrderStatusError,
)
from app.models.asset import Asset
from app.repositories.work_order_repository import (
    create_work_order,
    get_all_work_orders,
    get_work_order_by_id,
    get_work_order_for_update,
)
from app.schemas.work_order import WorkOrderCreate


# HU-05: Crear una orden de trabajo
def register_work_order(db: Session, data: WorkOrderCreate):
    asset = db.query(Asset).filter(
        Asset.id == data.asset_id
    ).first()

    if not asset:
        raise AssetNotFoundError(
            "El activo seleccionado no existe."
        )

    if asset.status != "Activo":
        raise InactiveAssetError(
            "No se pueden crear órdenes para un activo inactivo."
        )

    return create_work_order(db, data)


# HU-06: Consultar todas las órdenes
def list_work_orders(db: Session):
    return get_all_work_orders(db)


# HU-06: Consultar una orden
def find_work_order(db: Session, work_order_id: int):
    return get_work_order_by_id(db, work_order_id)


# HU-07: Actualizar el estado de una orden
def change_work_order_status(
    db: Session,
    work_order_id: int,
    new_status: str
):
    work_order = get_work_order_for_update(db, work_order_id)

    if not work_order:
        return None

    allowed_transitions = {
        "Pendiente": "En progreso",
        "En progreso": "Finalizada",
    }

    expected_status = allowed_transitions.get(work_order.status)

    if expected_status != new_status:
        raise InvalidWorkOrderStatusError(
            f"Transición no permitida. El siguiente estado debe ser: "
            f"{expected_status or 'ninguno'}."
        )

    work_order.status = new_status

    db.commit()
    db.refresh(work_order)

    return work_order