from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) >= 2

def test_create_task():
    response = client.post("/tasks", json={"title": "Practice with Copilot"})
    assert response.status_code == 201
    assert response.json()["title"] == "Practice with Copilot"

def test_complete_task():
    response = client.patch("/tasks/1")
    assert response.status_code == 200
    assert response.json()["completed"] is True
