# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: Result of the operation.

    Raises:
        ValueError: If operation is invalid.
        ZeroDivisionError: If division by zero is attempted.
    """
    operation = operation.strip().lower()  # Normalize input

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation.")
