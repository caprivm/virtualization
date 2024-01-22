"""
Description
=========================

This package contains the configuration files for the connection between the application and external tools such as databases (Postgres and Mongo), the task queuing system based on Celery and RabbitMQ, and the configuration for the logging system.

Examples:
    Import the package that has the configuration of the connection to the Mongo database:

    .. code-block:: python
        :linenos:

        from config.config_mongo import SettingsMongo
        from pymongo import MongoClient

    Next, to use this class in your code, you can do the following. This example shows how to connect to the Mongo database using the MongoClient class from the pymongo library:

    .. code-block:: python
        :linenos:

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


In the variable `mongodb_client` you will have the connection to the Mongo database. You can use this variable to perform operations on the database.
"""

from __future__ import absolute_import
from config.config_celery import app as celery_app

__all__ = ["celery_app"]
