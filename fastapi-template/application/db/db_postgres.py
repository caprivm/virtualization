from config.config_postgres import SettingsPostgres
from models.model_item import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import logging

settings = SettingsPostgres()

engine = create_engine(
    url=settings.sync_database_url, pool_pre_ping=True, echo=settings.db_echo_log
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
logging.info("Connected to postgres and created tables.")


def get_db() -> sessionmaker:
    """
    Get the database session for Postgres.

    :yield: Database session
    :rtype: sqlalchemy.orm.session.Session
    """
    database = session_local()
    try:
        yield database
    finally:
        database.close()
