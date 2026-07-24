from sqlmodel import SQLModel, Field


class TaskPublic(SQLModel):
    id: int = Field(default=None, primary_key=True)
    title: str | None = Field(index=True)
    done: bool = Field(default=False)


class Task(TaskPublic, table=True):
    pass
