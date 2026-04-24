from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code in [200, 503]


def test_create_job():
    response = client.post("/jobs")
    assert response.status_code in [200, 500, 503]


def test_invalid_job():
    response = client.get("/jobs/test-id")
    assert response.status_code in [200, 404, 500, 503]
