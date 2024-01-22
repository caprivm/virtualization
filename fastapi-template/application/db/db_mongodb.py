from config.config_mongo import SettingsMongo
from pymongo import MongoClient
import logging

mongodb_client = MongoClient(
    host=SettingsMongo.app_settings.get("mongodb_host"),
    port=SettingsMongo.app_settings.get("mongodb_port"),
    username=SettingsMongo.app_settings.get("username"),
    password=SettingsMongo.app_settings.get("password"),
    maxPoolSize=SettingsMongo.app_settings.get("max_pool_size"),
    minPoolSize=SettingsMongo.app_settings.get("min_pool_size"),
    uuidRepresentation="standard",
    connectTimeoutMS=10000,
)
logging.info("Connected to mongo.")


def get_db(db_client: MongoClient = mongodb_client):
    db_name = SettingsMongo.app_settings.get("db_name")
    return db_client[db_name]


def close_db_connect(db_client: MongoClient = mongodb_client) -> None:
    if db_client is None:
        logging.warning("Connection is None, nothing to close.")
        return
    db_client.close()
    db_client = None
    logging.info("Mongo connection closed.")
