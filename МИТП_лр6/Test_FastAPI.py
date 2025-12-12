from fastapi.testclient import TestClient
from FastAPI_ForTest import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_create_item():
    item_data = {"name": "Test Item", "price": 9.99}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Item created"
    assert data["item"]["name"] == "Test Item"

def test_list_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert "items" in response.json()
