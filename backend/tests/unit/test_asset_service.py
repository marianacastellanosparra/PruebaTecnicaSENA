
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.exceptions.asset_exceptions import DuplicateAssetError
from app.schemas.asset import AssetCreate
from app.services import asset_service


@pytest.fixture
def db():
    return MagicMock()


@pytest.fixture
def asset_data():
    return AssetCreate(
        name="Compresor",
        asset_type="Mecánico",
        location="Taller"
    )


def test_register_asset_success(db, asset_data, monkeypatch):
    db.query.return_value.filter.return_value.first.return_value = None
    expected = SimpleNamespace(id=1, name="Compresor")

    monkeypatch.setattr(
        asset_service, "create_asset", lambda db, data: expected
    )

    result = asset_service.register_asset(db, asset_data)

    assert result == expected


def test_register_asset_duplicate(db, asset_data):
    db.query.return_value.filter.return_value.first.return_value = (
        SimpleNamespace(id=1)
    )

    with pytest.raises(DuplicateAssetError):
        asset_service.register_asset(db, asset_data)


def test_list_assets(db, monkeypatch):
    expected = [SimpleNamespace(id=1), SimpleNamespace(id=2)]

    monkeypatch.setattr(
        asset_service, "get_all_assets", lambda db: expected
    )

    assert asset_service.list_assets(db) == expected


def test_find_asset(db, monkeypatch):
    expected = SimpleNamespace(id=1)

    monkeypatch.setattr(
        asset_service, "get_asset_by_id",
        lambda db, asset_id: expected
    )

    assert asset_service.find_asset(db, 1) == expected


def test_edit_asset_success(db, asset_data, monkeypatch):
    asset = SimpleNamespace(id=1)

    monkeypatch.setattr(
        asset_service, "get_asset_by_id",
        lambda db, asset_id: asset
    )
    db.query.return_value.filter.return_value.first.return_value = None

    expected = SimpleNamespace(id=1, name="Compresor")

    monkeypatch.setattr(
        asset_service, "update_asset",
        lambda db, current, data: expected
    )

    assert asset_service.edit_asset(db, 1, asset_data) == expected


def test_edit_asset_not_found(db, asset_data, monkeypatch):
    monkeypatch.setattr(
        asset_service, "get_asset_by_id",
        lambda db, asset_id: None
    )

    assert asset_service.edit_asset(db, 99, asset_data) is None


def test_edit_asset_duplicate(db, asset_data, monkeypatch):
    monkeypatch.setattr(
        asset_service, "get_asset_by_id",
        lambda db, asset_id: SimpleNamespace(id=1)
    )
    db.query.return_value.filter.return_value.first.return_value = (
        SimpleNamespace(id=2)
    )

    with pytest.raises(DuplicateAssetError):
        asset_service.edit_asset(db, 1, asset_data)


def test_disable_asset_success(db, monkeypatch):
    asset = SimpleNamespace(id=1)

    monkeypatch.setattr(
        asset_service, "get_asset_by_id",
        lambda db, asset_id: asset
    )

    expected = SimpleNamespace(id=1, status="Inactivo")

    monkeypatch.setattr(
        asset_service, "deactivate_asset",
        lambda db, current: expected
    )

    assert asset_service.disable_asset(db, 1) == expected


def test_disable_asset_not_found(db, monkeypatch):
    monkeypatch.setattr(
        asset_service, "get_asset_by_id",
        lambda db, asset_id: None
    )

    assert asset_service.disable_asset(db, 99) is None
