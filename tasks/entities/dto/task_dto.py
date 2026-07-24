from sqlmodel import SQLModel
from tasks.entities.task import TaskPublic


class TaskCreateDto(TaskPublic):
    pass


class TaskUpdateDTO(SQLModel):
    title: str | None
    done: bool | None
