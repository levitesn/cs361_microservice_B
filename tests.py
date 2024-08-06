from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_user():
    response = client.post("/create_user", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}


def test_create_existing_user():
    response = client.post("/create_user", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}


def test_login_success():
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}


def test_login_incorrect_password():
    response = client.post("/login", json={"username": "testuser", "password": "wrongpass"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect password"}


def test_login_user_not_found():
    response = client.post("/login", json={"username": "nonexistentuser", "password": "testpass"})
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
