def fibonacci_generator(n: int) -> list[int]:
    """
    fibonacci_generator _summary_

    :param n: _description_
    :type n: int
    :return: _description_
    :rtype: list[int]
    """
    fibonacci_sequence = []
    a, b = 0, 1

    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence
