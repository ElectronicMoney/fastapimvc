from fastapi.testclient import TestClient
from main import app


def create_client():
    client = TestClient(app)

    client.post("/v1/users", json={
        "first_name": "Test",
        "last_name": "Tester",
        "email": "test123@gmail.com",
        "username": "test12345",
        "password":"Test123",
        "confirmPassword": "Test123"
    })
    return client

# Create client
client = create_client()


def test_get_users():
    response = client.get("/v1/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
