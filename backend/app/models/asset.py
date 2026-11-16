from sqlalchemy import (
    CheckConstraint,
    Index,
    Integer,
    String,
    DateTime,
    func,
    text,
    column,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class Asset(Base):
    __tablename__ = "assets"

    # Identificador único del activo
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Información del activo
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    asset_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    # Estado inicial: Activo
    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Activo",
        server_default=text("'Activo'")
    )

    # Fecha generada automáticamente por PostgreSQL
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    # Restricciones e índice para proteger los datos
    __table_args__ = (
        CheckConstraint(
            "length(btrim(name)) > 0",
            name="ck_assets_name_not_blank"
        ),
        CheckConstraint(
            "length(btrim(asset_type)) > 0",
            name="ck_assets_type_not_blank"
        ),
        CheckConstraint(
            "length(btrim(location)) > 0",
            name="ck_assets_location_not_blank"
        ),
        CheckConstraint(
            "status IN ('Activo', 'Inactivo')",
            name="ck_assets_valid_status"
        ),
        Index(
            "uq_assets_normalized_identity",
            func.lower(func.btrim(column("name"))),
            func.lower(func.btrim(column("asset_type"))),
            func.lower(func.btrim(column("location"))),
            unique=True
        ),
    )