from fastapi.testclient import TestClient
from todo_api.main import app

client = TestClient(app)

def test_read_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_todo():
    response = client.post("/todos", json={"title": "Buy milk", "completed": False})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy milk"
    assert data["completed"] is False
    assert "id" in data
