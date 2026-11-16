from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.exceptions.work_order_exceptions import (
    AssetNotFoundError,
    InactiveAssetError,
    InvalidWorkOrderStatusError,
)
from app.schemas.work_order import (
    WorkOrderCreate,
    WorkOrderStatusUpdate,
    WorkOrderResponse,
)
from app.services.work_order_service import (
    register_work_order,
    list_work_orders,
    find_work_order,
    change_work_order_status,
)


router = APIRouter(
    prefix="/api/work-orders",
    tags=["Work Orders"]
)


# HU-05: Crear una orden
@router.post("", response_model=WorkOrderResponse, status_code=201)
def create_new_work_order(
    data: WorkOrderCreate,
    db: Session = Depends(get_db)
):
    try:
        return register_work_order(db, data)

    except AssetNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))

    except InactiveAssetError as error:
        raise HTTPException(status_code=409, detail=str(error))


# HU-06: Consultar todas las órdenes
@router.get("", response_model=list[WorkOrderResponse])
def get_work_orders(db: Session = Depends(get_db)):
    return list_work_orders(db)


# HU-06: Consultar una orden por ID
@router.get("/{work_order_id}", response_model=WorkOrderResponse)
def get_work_order(
    work_order_id: int,
    db: Session = Depends(get_db)
):
    work_order = find_work_order(db, work_order_id)

    if not work_order:
        raise HTTPException(
            status_code=404,
            detail="Orden de trabajo no encontrada."
        )

    return work_order


# HU-07: Actualizar el estado
@router.patch("/{work_order_id}/status", response_model=WorkOrderResponse)
def update_work_order_status(
    work_order_id: int,
    data: WorkOrderStatusUpdate,
    db: Session = Depends(get_db)
):
    try:
        work_order = change_work_order_status(
            db,
            work_order_id,
            data.status
        )

        if not work_order:
            raise HTTPException(
                status_code=404,
                detail="Orden de trabajo no encontrada."
            )

        return work_order

    except InvalidWorkOrderStatusError as error:
        raise HTTPException(status_code=409, detail=str(error))