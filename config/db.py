from typing import Annotated

from fastapi import Depends

from sqlmodel import create_engine, SQLModel, Session

db_filename: str = "development.db"

sqlite_url: str = f"sqlite:///{db_filename}"


connect_args: dict[str, bool] = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
