from schemas.schema_error import InternalError
import logging
import os


class SettingsMongo:
    """
    Class to define the settings of the Mongo Database.

    :raises InternalError: In the validation of the variables, this exception is raised if some variable is :code:`None` or not defined.
    """

    version = "1.0"
    title = "Mongo Variables"

    app_settings = {
        "db_name": os.getenv("MONGODB_DB", "fastapi-data"),
        "mongodb_host": os.getenv("MONGODB_HOSTNAME", "mongodb"),
        "mongodb_port": int(os.getenv("MONGODB_PORT", 27017)),
        "username": os.getenv("MONGODB_USERNAME", ""),
        "password": os.getenv("MONGODB_PASSWORD", ""),
        "max_pool_size": os.getenv("MONGODB_MAX_POOL_SIZE", 10),
        "min_pool_size": os.getenv("MONGODB_MIN_POOL_SIZE", 3),
    }

    @classmethod
    def app_settings_validate(cls):
        for k, v in cls.app_settings.items():
            if None is v:
                logging.error(f"Config variable error. {k} cannot be None")
                raise InternalError([{"message": "Server configure error"}])
            else:
                logging.info(f"Config variable {str(k)} is {str(v)}")
