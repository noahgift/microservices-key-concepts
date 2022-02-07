from fastapi import FastAPI
from fastapi.testclient import TestClient
from mainFastApi import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_read_add():
    response = client.get("/add/2/2")
    assert response.status_code == 200
    assert response.json() == {"total": 4}