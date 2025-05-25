def square(x: float | int) -> (float | int):
    return x * x

def add(a: float | int, b: float | int) -> (float | int):
    return a + b

def subtract(a: float | int, b: float | int) -> (float | int):
    # I've added this bug to see...
    # if the test workflow run will fail...
    # if failed tests occured.
    return a + b # intentional subtraction bug

def multiply(a: float | int, b: float | int) -> (float | int):
    return a * b

def divide(a: float | int, b: float | int) -> (float | int):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def module(a: int, b: int) -> int:
    return a % b # this function was uncovered because i didn't write a test for this
