from pydantic import BaseModel

from tasks.entities.task import TaskPublic


class TaskCreateDto(TaskPublic):
    pass


class TaskUpdateDTO(BaseModel):
    title: str | None
    done: bool | None
