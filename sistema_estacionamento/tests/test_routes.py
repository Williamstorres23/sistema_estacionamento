from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Sistema de estacionamento rodando"}

def test_vehicles_route():
    response = client.get("/vehicles/")
    assert response.status_code in [200, 404]  # Se não houver veículos, pode retornar 404
