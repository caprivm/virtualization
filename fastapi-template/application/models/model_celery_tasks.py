from config.config_celery import app
import time


@app.task(exchange="celery")
def add_numbers(x: int, y: int) -> int:
    """
    Function to add two integer numbers.

    :param x: First number to add.
    :type x: int
    :param y: Second number to add.
    :type y: int
    :return: Addition of the two numbers.
    :rtype: int
    """
    time.sleep(5)
    result = x + y
    return result
