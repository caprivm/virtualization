"""
=========================================
ArithmeticOperations Class Documentation
=========================================

.. contents::
   :local:

ArithmeticOperations Class
==========================

The `ArithmeticOperations` class provides a simple interface for performing basic arithmetic operations, including addition, subtraction, multiplication, and division. It is designed to handle integer operands and offers a convenient way to perform common mathematical calculations.

Initialization
--------------

To create an instance of the `ArithmeticOperations` class, provide two integer values as parameters during initialization:

.. code-block:: python

   calculator = ArithmeticOperations(10, 2)

The constructor validates that both provided values are integers. If either value is not an integer, a `ValueError` will be raised.

Methods
-------

### `add()`

Adds the two initialized numbers and returns the result.

.. code-block:: python

   result = calculator.add()

### `subtract()`

Subtracts the second initialized number from the first and returns the result.

.. code-block:: python

   result = calculator.subtract()

### `multiply()`

Multiplies the two initialized numbers and returns the result.

.. code-block:: python

   result = calculator.multiply()

### `divide()`

Divides the first initialized number by the second. Raises a `ValueError` if attempting to divide by zero.

.. code-block:: python

   result = calculator.divide()

Example Usage
-------------

Here is an example demonstrating the usage of the `ArithmeticOperations` class:

.. code-block:: python

  # Valid initialization
  calculator = ArithmeticOperations(10, 2)
  print(f"Addition: {calculator.add()}")
  print(f"Subtraction: {calculator.subtract()}")
  print(f"Multiplication: {calculator.multiply()}")
  print(f"Division: {calculator.divide()}")

Note: The example showcases both valid and invalid initializations, providing a clear understanding of how the class handles integer validation.

Enjoy using the `ArithmeticOperations` class for your basic arithmetic needs!
"""
