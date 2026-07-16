from pydantic import BaseModel


class TaskPublic(BaseModel):
    title: str
    done: bool = False


class Task(TaskPublic):
    id: int
