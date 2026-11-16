from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AssetCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    asset_type: str = Field(min_length=1, max_length=50)
    location: str = Field(min_length=1, max_length=150)

    status: Literal["Activo", "Inactivo"] = "Activo"

    @field_validator("name", "asset_type", "location", mode="before")
    @classmethod
    def clean_text(cls, value):
        if isinstance(value, str):
            return value.strip()
        return value


class AssetResponse(BaseModel):
    id: int
    name: str
    asset_type: str
    location: str
    status: Literal["Activo", "Inactivo"]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)