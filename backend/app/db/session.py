from collection.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

#DataBase connection URL
DATABASE_URL = settings.database_url

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True, # Set to True to enable SQL query logging for debugging purposes
    pool_pre_ping=True,  # Enable connection pool pre-ping to check connections before using them
)

#Create a session factory

SessionLocal = sessionmaker (
    bind=engine,
    autoflush=False,  # Disable automatic flushing of changes to the database
    autocommit=False,  # Disable automatic committing of transactions
)


def get_db():
    """
    Provide a database session and close it after usage. This function is typically used as a dependency in FastAPI routes.
    """

    db = SessionLocal()

    try:
        yield db  # Yield the database session to the caller
    finally:
        db.close()  # Ensure the database session is closed after usage
