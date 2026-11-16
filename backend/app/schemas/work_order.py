from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.schemas.asset import AssetResponse


class WorkOrderCreate(BaseModel):
    asset_id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=1)
    priority: Literal["Baja", "Media", "Alta"]

    @field_validator("title", "description", mode="before")
    @classmethod
    def clean_text(cls, value):
        if isinstance(value, str):
            return value.strip()
        return value


class WorkOrderStatusUpdate(BaseModel):
    status: Literal["Pendiente", "En progreso", "Finalizada"]


class WorkOrderResponse(BaseModel):
    id: int
    asset_id: int
    title: str
    description: str
    priority: Literal["Baja", "Media", "Alta"]
    status: Literal["Pendiente", "En progreso", "Finalizada"]
    created_at: datetime
    asset: AssetResponse

    model_config = ConfigDict(from_attributes=True)