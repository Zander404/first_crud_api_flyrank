from typing import List

from fastapi import APIRouter


task_list: List[dict] = [
    {"id": 1, "title": "Task 1", "done": True},
    {"id": 2, "title": "Task 2", "done": False},
    {"id": 3, "title": "Task 3", "done": True},
]


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
def get_all():
    return task_list


@router.get("/{id}")
def get_one(id: int):

    task = [task for task in task_list if task["id"] == id]

    if not task:
        return {"error": f"Task {id} not found"}

    return task
