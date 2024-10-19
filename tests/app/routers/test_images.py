import os
from pathlib import Path
from typing import Any

import pytest
from fastapi import BackgroundTasks
from fastapi.testclient import TestClient

from aittor.app.api.dependencies import ApiDependencies
from aittor.app.api_app import app
from aittor.app.services.board_records.board_records_common import BoardRecord
from aittor.app.services.operator import Operator


@pytest.fixture(autouse=True, scope="module")
def client(app_root_dir: Path) -> TestClient:
    os.environ["APP_ROOT"] = app_root_dir.as_posix()
    return TestClient(app)


class MockApiDependencies(ApiDependencies):
    operator: Operator

    def __init__(self, operator) -> None:
        self.operator = operator


def test_download_images_from_list(monkeypatch: Any, mock_operator: Operator, client: TestClient) -> None:
    prepare_download_images_test(monkeypatch, mock_operator)

    response = client.post("/api/v1/images/download", json={"image_names": ["test.png"]})
    json_response = response.json()
    assert response.status_code == 202
    assert json_response["bulk_download_item_name"] == "test.zip"


def test_download_images_from_board_id_empty_image_name_list(
    monkeypatch: Any, mock_operator: Operator, client: TestClient
) -> None:
    expected_board_name = "test"

    def mock_get(*args, **kwargs):
        return BoardRecord(board_id="12345", board_name=expected_board_name, created_at="None", updated_at="None")

    monkeypatch.setattr(mock_operator.services.board_records, "get", mock_get)
    prepare_download_images_test(monkeypatch, mock_operator)

    response = client.post("/api/v1/images/download", json={"board_id": "test"})
    json_response = response.json()
    assert response.status_code == 202
    assert json_response["bulk_download_item_name"] == "test.zip"


def prepare_download_images_test(monkeypatch: Any, mock_operator: Operator) -> None:
    monkeypatch.setattr("aittor.app.api.routers.images.ApiDependencies", MockApiDependencies(mock_operator))
    monkeypatch.setattr(
        "aittor.app.api.routers.images.ApiDependencies.operator.services.bulk_download.generate_item_id",
        lambda arg: "test",
    )

    def mock_add_task(*args, **kwargs):
        return None

    monkeypatch.setattr(BackgroundTasks, "add_task", mock_add_task)


def test_download_images_with_empty_image_list_and_no_board_id(
    monkeypatch: Any, mock_operator: Operator, client: TestClient
) -> None:
    prepare_download_images_test(monkeypatch, mock_operator)

    response = client.post("/api/v1/images/download", json={"image_names": []})

    assert response.status_code == 400


def test_get_bulk_download_image(tmp_path: Path, monkeypatch: Any, mock_operator: Operator, client: TestClient) -> None:
    mock_file: Path = tmp_path / "test.zip"
    mock_file.write_text("contents")

    monkeypatch.setattr(mock_operator.services.bulk_download, "get_path", lambda x: str(mock_file))
    monkeypatch.setattr("aittor.app.api.routers.images.ApiDependencies", MockApiDependencies(mock_operator))

    def mock_add_task(*args, **kwargs):
        return None

    monkeypatch.setattr(BackgroundTasks, "add_task", mock_add_task)

    response = client.get("/api/v1/images/download/test.zip")

    assert response.status_code == 200
    assert response.content == b"contents"


def test_get_bulk_download_image_not_found(monkeypatch: Any, mock_operator: Operator, client: TestClient) -> None:
    monkeypatch.setattr("aittor.app.api.routers.images.ApiDependencies", MockApiDependencies(mock_operator))

    def mock_add_task(*args, **kwargs):
        return None

    monkeypatch.setattr(BackgroundTasks, "add_task", mock_add_task)

    response = client.get("/api/v1/images/download/test.zip")

    assert response.status_code == 404


def test_get_bulk_download_image_image_deleted_after_response(
    monkeypatch: Any, mock_operator: Operator, tmp_path: Path, client: TestClient
) -> None:
    mock_file: Path = tmp_path / "test.zip"
    mock_file.write_text("contents")

    monkeypatch.setattr(mock_operator.services.bulk_download, "get_path", lambda x: str(mock_file))
    monkeypatch.setattr("aittor.app.api.routers.images.ApiDependencies", MockApiDependencies(mock_operator))

    client.get("/api/v1/images/download/test.zip")

    assert not (tmp_path / "test.zip").exists()
