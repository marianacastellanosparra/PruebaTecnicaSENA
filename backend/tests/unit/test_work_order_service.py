
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.exceptions.work_order_exceptions import (
    AssetNotFoundError,
    InactiveAssetError,
    InvalidWorkOrderStatusError,
)
from app.schemas.work_order import WorkOrderCreate
from app.services import work_order_service


@pytest.fixture
def db():
    return MagicMock()


@pytest.fixture
def order_data():
    return WorkOrderCreate(
        asset_id=1,
        title="Mantenimiento preventivo",
        description="Revisión general del equipo",
        priority="Alta"
    )


def test_register_work_order_success(db, order_data, monkeypatch):
    db.query.return_value.filter.return_value.first.return_value = (
        SimpleNamespace(id=1, status="Activo")
    )

    expected = SimpleNamespace(id=1, status="Pendiente")

    monkeypatch.setattr(
        work_order_service, "create_work_order",
        lambda db, data: expected
    )

    assert work_order_service.register_work_order(db, order_data) == expected


def test_register_work_order_asset_not_found(db, order_data):
    db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(AssetNotFoundError):
        work_order_service.register_work_order(db, order_data)


def test_register_work_order_inactive_asset(db, order_data):
    db.query.return_value.filter.return_value.first.return_value = (
        SimpleNamespace(id=1, status="Inactivo")
    )

    with pytest.raises(InactiveAssetError):
        work_order_service.register_work_order(db, order_data)


def test_list_work_orders(db, monkeypatch):
    expected = [SimpleNamespace(id=1), SimpleNamespace(id=2)]

    monkeypatch.setattr(
        work_order_service, "get_all_work_orders",
        lambda db: expected
    )

    assert work_order_service.list_work_orders(db) == expected


def test_find_work_order(db, monkeypatch):
    expected = SimpleNamespace(id=1)

    monkeypatch.setattr(
        work_order_service, "get_work_order_by_id",
        lambda db, order_id: expected
    )

    assert work_order_service.find_work_order(db, 1) == expected


def test_change_status_pending_to_in_progress(db, monkeypatch):
    order = SimpleNamespace(id=1, status="Pendiente")

    monkeypatch.setattr(
        work_order_service, "get_work_order_for_update",
        lambda db, order_id: order
    )

    result = work_order_service.change_work_order_status(
        db, 1, "En progreso"
    )

    assert result.status == "En progreso"
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(order)


def test_change_status_in_progress_to_finished(db, monkeypatch):
    order = SimpleNamespace(id=1, status="En progreso")

    monkeypatch.setattr(
        work_order_service, "get_work_order_for_update",
        lambda db, order_id: order
    )

    result = work_order_service.change_work_order_status(
        db, 1, "Finalizada"
    )

    assert result.status == "Finalizada"
    db.commit.assert_called_once()


def test_change_status_invalid_transition(db, monkeypatch):
    order = SimpleNamespace(id=1, status="Pendiente")

    monkeypatch.setattr(
        work_order_service, "get_work_order_for_update",
        lambda db, order_id: order
    )

    with pytest.raises(InvalidWorkOrderStatusError):
        work_order_service.change_work_order_status(
            db, 1, "Finalizada"
        )

    db.commit.assert_not_called()


def test_change_status_order_not_found(db, monkeypatch):
    monkeypatch.setattr(
        work_order_service, "get_work_order_for_update",
        lambda db, order_id: None
    )

    result = work_order_service.change_work_order_status(
        db, 99, "En progreso"
    )

    assert result is None
    db.commit.assert_not_called()
