from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version_default(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    assert client.get("/version").json() == {"version": "local"}


def test_version_from_environment(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "abc123")
    assert client.get("/version").json() == {"version": "abc123"}


def test_unknown_route():
    assert client.get("/missing").status_code == 404


def test_health_is_read_only():
    assert client.post("/health").status_code == 405
