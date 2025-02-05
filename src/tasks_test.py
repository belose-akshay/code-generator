from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_task_success():
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "status": "pending",
        "due_date": "2023-12-31",
    }
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "This is a test task"
    assert response.json()["status"] == "pending"
    assert response.json()["due_date"] == "2023-12-31"


def test_create_task_missing_title():
    task_data = {
        "description": "This is a test task",
        "status": "pending",
        "due_date": "2023-12-31",
    }
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"
    assert response.json()["detail"][0]["loc"] == ["body", "title"]


def test_get_tasks_empty():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_tasks_with_data():
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "status": "pending",
        "due_date": "2023-12-31",
    }
    client.post("/tasks/", json=task_data)  # Create a task first
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Test Task"


def test_get_task_by_id_success():
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "status": "pending",
        "due_date": "2023-12-31",
    }
    response = client.post("/tasks/", json=task_data)
    task_id = response.json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"


def test_get_task_by_id_not_found():
    response = client.get("/tasks/100")  # Assuming no task with ID 100
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task_success():
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "status": "pending",
        "due_date": "2023-12-31",
    }
    response = client.post("/tasks/", json=task_data)
    task_id = response.json()["id"]
    updated_data = {
        "title": "Updated Test Task",
        "description": "This is an updated test task",
        "status": "completed",
        "due_date": "2024-01-01",
    }
    response = client.put(f"/tasks/{task_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Task"
    assert response.json()["description"] == "This is an updated test task"
    assert response.json()["status"] == "completed"
    assert response.json()["due_date"] == "2024-01-01"


def test_update_task_not_found():
    updated_data = {
        "title": "Updated Test Task",
        "description": "This is an updated test task",
        "status": "completed",
        "due_date": "2024-01-01",
    }
    response = client.put("/tasks/100", json=updated_data)  # Assuming no task with ID 100
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_delete_task_success():
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "status": "pending",
        "due_date": "2023-12-31",
    }
    response = client.post("/tasks/", json=task_data)
    task_id = response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Task deleted successfully"}


def test_delete_task_not_found():
    response = client.delete("/tasks/100")  # Assuming no task with ID 100
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"