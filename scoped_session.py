from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


@contextmanager
def scoped_session_maker(
    db_conn: str,
    pool_size: int = 2,
) -> Generator[Session, None, None]:
    """
    SQLAlchemy scoped_session context manager, for thread safe session management.
    Example:
        with scoped_session_maker("sqlite://") as session:
            result = session.query(Model).one()
    """
    # engine and or sessionmaker could be passed in
    # but for the sake of clarity, they're fine here.
    engine = create_engine(db_conn, pool_size=pool_size)
    sc_session = scoped_session(sessionmaker(engine))
    session = sc_session()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        sc_session.remove()
        engine.dispose()  # may or not be needed. docs not clear
