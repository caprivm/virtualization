class ArithmeticOperations:
    """
    Class to perform arithmetic operations on two integer numbers.
    """

    def __init__(self, a: int, b: int) -> None:
        """
        Function to initialize the class.

        :param a: First number that will be used in the operations.
        :type a: int
        :param b: Second number that will be used in the operations.
        :type b: int
        :raises ValueError: Error raised when one of the numbers is not an integer.
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both numbers must be integers.")
        self.number_1 = a
        self.number_2 = b

    def add_numbers(self) -> int:
        """
        Function to add two integer numbers.

        :return: The sum of the two numbers.
        :rtype: int
        """
        return self.number_1 + self.number_2

    def subtract_numbers(self) -> int:
        """
        Function to subtract two integer numbers.

        :return: The difference of the two numbers.
        :rtype: int
        """
        return self.number_1 - self.number_2

    def multiply_numbers(self) -> int:
        """
        Function to multiply two integer numbers.

        :return: The product of the two numbers.
        :rtype: int
        """
        return self.number_1 * self.number_2

    def divide_numbers(self) -> float:
        """
        Function to divide two integer numbers.

        :raises ValueError: Error raised when the second number is zero.
        :return: The quotient of the two numbers.
        :rtype: float
        """
        if self.number_2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.number_1 / self.number_2
