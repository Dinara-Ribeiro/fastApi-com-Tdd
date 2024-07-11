import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_database

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    # Limpar o banco de dados antes de cada teste
    db = get_database()
    db["items"].drop()

def test_create_item():
    response = client.post("/items/", json={"name": "item1", "description": "An item"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "item1"
    assert data["description"] == "An item"

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
