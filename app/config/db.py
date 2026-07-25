from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends

from sqlmodel import create_engine, SQLModel, Session

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgres"):
    if "@db:" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("@db:", "@localhost:")
        engine = create_engine(DATABASE_URL)
else:
    connect_args: dict[str, bool] = {"check_same_thread": False}
    engine = create_engine("testing.db", connect_args=connect_args)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
