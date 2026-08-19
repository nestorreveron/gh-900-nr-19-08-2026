from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.models import Base

_engine = None
SessionLocal: sessionmaker[Session] | None = None


def init_database(database_url: str) -> None:
    global _engine, SessionLocal
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    _engine = create_engine(database_url, connect_args=connect_args, future=True)
    SessionLocal = sessionmaker(bind=_engine, autoflush=False, expire_on_commit=False, future=True)
    Base.metadata.create_all(_engine)


@contextmanager
def get_session() -> Generator[Session, None, None]:
    if SessionLocal is None:
        raise RuntimeError("Database has not been initialized")
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
