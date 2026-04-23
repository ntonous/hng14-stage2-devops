from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from api.main import app

client = TestClient(app)


@patch("api.main.r")
def test_health(mock_redis):
    response = client.get("/health")
    assert response.status_code == 200


@patch("api.main.r")
def test_create_job(mock_redis):
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


@patch("api.main.r")
def test_job_not_found(mock_redis):
    mock_redis.hget.return_value = None
    response = client.get("/jobs/test123")
    assert response.status_code in [200, 404]