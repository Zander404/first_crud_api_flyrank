from typing import List

from fastapi import APIRouter, HTTPException, status

from app.config.db import SessionDep
from app.tasks.entities.dto.task_dto import TaskCreateDto, TaskUpdateDTO
from app.tasks.entities.task import Task, TaskPublic
from sqlmodel import select


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=List[Task], status_code=status.HTTP_200_OK)
def get_all(session: SessionDep) -> list[Task]:
    return session.exec(select(Task)).all()


@router.get("/{id}", response_model=TaskPublic, status_code=status.HTTP_200_OK)
def get_one(id: int, session: SessionDep):

    task = session.get_one(Task, id)

    if not task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")

    return task


@router.post("", response_model=TaskPublic, status_code=status.HTTP_201_CREATED)
async def create_task(createDTO: TaskCreateDto, session: SessionDep):

    if not createDTO.title:
        raise HTTPException(status_code=400, detail="Task don't have a title!")

    task_data = Task.model_validate(createDTO)

    session.add(task_data)
    session.commit()
    session.refresh(task_data)
    return task_data


@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task(id: int, updateDTO: TaskUpdateDTO, session: SessionDep):

    task_db = session.get_one(Task, id)

    if not task_db:
        raise HTTPException(status_code=404, detail=f"Task with {id} not found!")

    update_data = updateDTO.model_dump(exclude_unset=True)

    if "title" in update_data and not update_data["title"].strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty!")

    task_db.sqlmodel_update(update_data)

    session.add(task_db)
    session.commit()
    session.refresh(task_db)

    return task_db


@router.delete("{id}", status_code=204)
def delete_task(id: int, session: SessionDep):

    task = session.get_one(Task, id)

    if not task:
        raise HTTPException(status_code=404, detail=f"Task with {id} not found!")

    session.delete(task)
    session.commit()

    return
