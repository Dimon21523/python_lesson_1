import os

from sqlalchemy import create_engine


def get_engine():
    """
    Берем строку подключения из переменной окружения DATABASE_URL.
    Пример:
    postgresql://postgres:YOUR_PASSWORD@localhost:5432/school_db
    """
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError(
            "DATABASE_URL is not set. Example: "
            "postgresql://postgres:YOUR_PASSWORD@localhost:5432/school_db"
        )
    return create_engine(db_url, echo=False, future=True)
