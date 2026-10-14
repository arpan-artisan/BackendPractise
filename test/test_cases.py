from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_reading():
    response = client.post(
        "/readings",
        json={
            "sensor_id": 1,
            "temperature": 45,
            "unit": "C"
        }
    )

    assert response.status_code == 200
    assert response.json() == {"state": "alert"}

def test_normal_temperature():
    response = client.post(
        "/readings",
        json={
            "sensor_id": 2,
            "temperature": 35,
            "unit": "C"
        }
    )

    assert response.status_code == 200
    assert response.json() == {"state": "normal"}

def test_threshold_boundary():
    response = client.post(
        "/readings",
        json={
            "sensor_id": 3,
            "temperature": 40,
            "unit": "C"
        }
    )

    assert response.status_code == 200
    assert response.json() == {"state": "normal"}

def test_fahrenheit_alert():
    response = client.post(
        "/readings",
        json={
            "sensor_id": 4,
            "temperature": 105,
            "unit": "F"
        }
    )

    assert response.status_code == 200
    assert response.json() == {"state": "alert"}

def test_invalid_unit():
    response = client.post(
        "/readings",
        json={
            "sensor_id": 5,
            "temperature": 30,
            "unit": "K"
        }
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "The parameter must be either 'C' or 'F'."}

def test_missing_temperature():
    response = client.post(
        "/readings",
        json={
            "sensor_id": 6,
            "unit": "C"
        }
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "temperature"],
                "msg": "Field required",
                "type": "missing",
                "input": {'sensor_id': 6, 'unit': 'C'}
            }
        ]
    }
