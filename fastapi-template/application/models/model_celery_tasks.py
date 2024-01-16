from config.config_celery import app
from datetime import datetime, timedelta
from uuid import UUID
import logging


@app.task(exchange="celery")
def add_numbers(x: int, y: int) -> int | None:
    """
    Function to add two integer numbers.

    :param x: First number to add.
    :type x: int
    :param y: Second number to add.
    :type y: int
    :raises Exception: If something happen.
    :return: Addition of the two numbers.
    :rtype: int
    """
    try:
        logging.info(f"Adding the numbers: {x} + {y}")
        result = x + y
    except Exception as e:
        logging.error(f"Error adding the numbers: {e}")
        result = None
    return result
