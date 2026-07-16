from typing import List

from fastapi import APIRouter, HTTPException

from tasks.entities.dto.task_dto import TaskCreateDto
from tasks.entities.task import Task


task_list: List[Task] = [
    Task(id=1, title="Task 1", done=True),
    Task(id=2, title="Task 2", done=False),
    Task(id=3, title="Task 3", done=True),
]


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("")
def get_all():
    return task_list


@router.get("/{id}")
def get_one(id: int):

    task = [task for task in task_list if task["id"] == id]

    if not task:
        return {"error": f"Task {id} not found"}

    return task


@router.post("")
async def create_task(createDTO: TaskCreateDto):

    if not createDTO.title:
        return HTTPException(status_code=400, detail="Task don't have a title!")

    next_id: int = max([t.id for t in task_list], default=0) + 1
    task = Task(id=next_id, done=False, **createDTO.model_dump())
    task_list.append(task)

    return task
