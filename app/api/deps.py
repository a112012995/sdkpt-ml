from typing import Generator

from app.db.session import SessionLocal
from app import crud, models, schemas


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
