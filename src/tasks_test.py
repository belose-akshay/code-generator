import pytest
from tasks import router  # Assuming your API code is in "your_api.py"

# Sample task data
task1 = {"title": "Task 1", "description": "First task", "status": "pending", "due_date": "2023-11-20"}
task2 = {"title": "Task 2", "status": "completed", "due_date": "2023-11-23"}

def test_create_task():
    # Create a new task
    response = router.post("/", json=task1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == task1["title"]
    assert data["description"] == task1["description"]
    assert data["status"] == task1["status"]
    assert data["due_date"] == task1["due_date"]

def test_create_task_missing_fields():
    # Create a task with missing fields
    response = router.post("/", json={"title": "Task 3"})
    assert response.status_code == 422

def test_get_tasks():
    # Get all tasks
    response = router.get("/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["title"] == task1["title"]
    assert data[1]["id"] == 2
    assert data[1]["title"] == task2["title"]

def test_get_task_by_id():
    # Get task by ID
    response = router.get("/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == task1["title"]

def test_get_nonexistent_task():
    # Get non-existent task
    response = router.get("/3")
    assert response.status_code == 404

def test_update_task():
    # Update existing task
    updated_task = {"title": "Updated Task 1", "status": "completed"}
    response = router.put("/1", json=updated_task)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == updated_task["title"]
    assert data["status"] == updated_task["status"]

def test_update_nonexistent_task():
    # Update non-existent task
    response = router.put("/3", json={"title": "Task 3"})
    assert response.status_code == 404

def test_delete_task():
    # Delete task
    response = router.delete("/1")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Task deleted successfully"

def test_delete_nonexistent_task():
    # Delete non-existent task
    response = router.delete("/3")
    assert response.status_code == 404

import pytest
def test_create_task():
    # Create a new task
    response = router.post("/", json=task1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == task1["title"]
    assert data["description"] == task1["description"]
    assert data["status"] == task1["status"]
    assert data["due_date"] == task1["due_date"]

import pytest
def test_create_task_missing_fields():
    # Create a task with missing fields
    response = router.post("/", json={"title": "Task 3"})
    assert response.status_code == 422

import pytest
def test_get_tasks():
    # Get all tasks
    response = router.get("/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["title"] == task1["title"]
    assert data[1]["id"] == 2
    assert data[1]["title"] == task2["title"]

import pytest
def test_get_task_by_id():
    # Get task by ID
    response = router.get("/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == task1["title"]

import pytest
def test_get_nonexistent_task():
    # Get non-existent task
    response = router.get("/3")
    assert response.status_code == 404

import pytest
def test_update_task():
    # Update existing task
    updated_task = {"title": "Updated Task 1", "status": "completed"}
    response = router.put("/1", json=updated_task)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == updated_task["title"]
    assert data["status"] == updated_task["status"]

import pytest
def test_update_nonexistent_task():
    # Update non-existent task
    response = router.put("/3", json={"title": "Task 3"})
    assert response.status_code == 404

import pytest
def test_delete_task():
    # Delete task
    response = router.delete("/1")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Task deleted successfully"

import pytest
def test_delete_nonexistent_task():
    # Delete non-existent task
    response = router.delete("/3")
    assert response.status_code == 404
