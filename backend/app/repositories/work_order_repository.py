from sqlalchemy.orm import Session, joinedload

from app.models.work_order import WorkOrder
from app.schemas.work_order import WorkOrderCreate


def create_work_order(db: Session, data: WorkOrderCreate):
    work_order = WorkOrder(**data.model_dump())

    db.add(work_order)
    db.commit()
    db.refresh(work_order)

    return work_order


def get_all_work_orders(db: Session):
    return (
        db.query(WorkOrder)
        .options(joinedload(WorkOrder.asset))
        .order_by(WorkOrder.id)
        .all()
    )


def get_work_order_by_id(db: Session, work_order_id: int):
    return (
        db.query(WorkOrder)
        .options(joinedload(WorkOrder.asset))
        .filter(WorkOrder.id == work_order_id)
        .first()
    )


def get_work_order_for_update(db: Session, work_order_id: int):
    return (
        db.query(WorkOrder)
        .filter(WorkOrder.id == work_order_id)
        .with_for_update()
        .first()
    )