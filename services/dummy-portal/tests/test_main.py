import pytest
from fastapi.testclient import TestClient
from src.main import app


def test_root():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200

    assert response.headers["content-type"].lower().startswith("application/json")


def test_healtz():
    client = TestClient(app)
    response = client.get("/healthz")

    assert response.status_code == 200

    assert response.headers["content-type"].lower().startswith("text/plain")