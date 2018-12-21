from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from common_consumer.settings import DatabaseConfig

engine = create_engine(DatabaseConfig.get_uri())


@contextmanager
def async_session() -> scoped_session:
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
