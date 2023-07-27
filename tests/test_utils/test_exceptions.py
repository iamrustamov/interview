from fastapi import status
from fastapi.testclient import TestClient

from app.main import app


def test_validation_exception_handler():
    client = TestClient(app)

    data = {
        "amount": 1000,
        "date": "01.01.2023",
        "periods": 12,
        "rate": 5.0
    }
    response = client.post("/api/v1/deposit/calculate", json=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"error": "Field body.amount should be an integer between 10000 and 3000000;"}