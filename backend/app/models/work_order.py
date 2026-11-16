from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class WorkOrder(Base):
    __tablename__ = "work_orders"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    asset_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("assets.id", ondelete="RESTRICT"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Pendiente",
        server_default=text("'Pendiente'")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    asset = relationship("Asset")

    __table_args__ = (
        CheckConstraint(
            "length(btrim(title)) > 0",
            name="ck_work_orders_title_not_blank"
        ),
        CheckConstraint(
            "length(btrim(description)) > 0",
            name="ck_work_orders_description_not_blank"
        ),
        CheckConstraint(
            "priority IN ('Baja', 'Media', 'Alta')",
            name="ck_work_orders_valid_priority"
        ),
        CheckConstraint(
            "status IN ('Pendiente', 'En progreso', 'Finalizada')",
            name="ck_work_orders_valid_status"
        ),
    )