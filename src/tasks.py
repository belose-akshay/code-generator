from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

from typing import List, Optional

router = APIRouter(prefix="/tasks", tags=["tasks"])

# In-memory task list

tasks = []

task_counter = 1


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    due_date: str


@router.post("/", response_model=Task)
def create_task(task: Task):
    global task_counter
    task.id = task_counter
    task_counter += 1
    tasks.append(task)
    return task


@router.get("/", response_model=List[Task])
def get_tasks():
    return tasks


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):

        if task.id == task_id:
            tasks[i] = updated_task

            tasks[i].id = task_id  # Preserve the task ID

            return tasks[i]

    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}")
def delete_task(task_id: int):
    global tasks

    tasks = [task for task in tasks if task.id != task_id]

    return {"detail": "Task deleted successfully"}
