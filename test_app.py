import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_create_task(client):
    response = client.post("/tasks", json={"title": "New Task"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "New Task"

def test_update_task(client):
    response = client.put("/tasks/1", json={"completed": True})
    assert response.status_code == 200
    assert response.get_json()["completed"] is True

def test_delete_task(client):
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Task deleted"
