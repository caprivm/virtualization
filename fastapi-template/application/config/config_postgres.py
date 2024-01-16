from pydantic_settings import BaseSettings
import os


class SettingsPostgres(BaseSettings):
    """
    Class to define the settings of the Postgres Database.

    :param BaseSettings: Pydantic BaseSettings
    :type BaseSettings: BaseSettings
    """

    postgres_server: str = os.getenv("POSTGRES_HOSTNAME", "postgres")
    postgres_port: str = os.getenv("POSTGRES_PORT", "5432")
    postgres_user: str = os.getenv("POSTGRES_USERNAME", "postgres")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    postgres_db: str = os.getenv("POSTGRES_DB", "fastapi-data")
    db_echo_log: bool = os.getenv("POSRGRES_ECHO_LOG", False)

    @property
    def sync_database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"

    class Config:
        case_sensitive = True
