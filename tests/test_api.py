from fastapi.testclient import TestClient
from unittest.mock import patch

from api.main import app

client = TestClient(app)


@patch("api.main.r")
def test_health(mock_redis):
    mock_redis.ping.return_value = True
    response = client.get("/health")
    assert response.status_code == 200


@patch("api.main.r")
def test_create_job(mock_redis):
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = 1

    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


@patch("api.main.r")
def test_invalid_job(mock_redis):
    mock_redis.hget.return_value = None

    response = client.get("/jobs/test-id")
    assert response.status_code == 404
