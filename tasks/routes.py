from typing import List

from fastapi import APIRouter, HTTPException, status

from tasks.entities.dto.task_dto import TaskCreateDto, TaskUpdateDTO
from tasks.entities.task import Task, TaskPublic


task_list: List[Task] = [
    Task(id=1, title="Task 1", done=True),
    Task(id=2, title="Task 2", done=False),
    Task(id=3, title="Task 3", done=True),
]


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=List[Task], status_code=status.HTTP_200_OK)
def get_all():
    return task_list


@router.get("/{id}", response_model=TaskPublic, status_code=status.HTTP_200_OK)
def get_one(id: int):

    task = next((t for t in task_list if t.id == id), None)

    if not task:
        return {"error": f"Task {id} not found"}

    return task


@router.post("", response_model=TaskPublic, status_code=status.HTTP_201_CREATED)
async def create_task(createDTO: TaskCreateDto):

    if not createDTO.title:
        raise HTTPException(status_code=400, detail="Task don't have a title!")

    next_id: int = max([t.id for t in task_list], default=0) + 1
    task = Task(id=next_id, done=False, **createDTO.model_dump())
    task_list.append(task)

    return task


@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task(id: int, updateDTO: TaskUpdateDTO):

    task = next((t for t in task_list if t.id == id), None)

    if not task:
        raise HTTPException(status_code=404, detail=f"Task with {id} not found!")

    update_data = updateDTO.model_dump(exclude_unset=True)

    if "title" in update_data and not update_data["title"].strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty!")

    task_dict = task.model_dump()

    task_dict.update(update_data)

    updated_task = Task(**task_dict)

    index = task_list.index(task)

    task_list[index] = updated_task

    return update_data


@router.delete("{id}", status_code=204)
def delete_task(id: int):

    task = next((t for t in task_list if t.id == id), None)

    if not task:
        raise HTTPException(status_code=404, detail=f"Task with {id} not found!")

    return task_list.remove(task)
