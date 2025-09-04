def square(x: float | int) -> (float | int):
    return x * x

def add(a: float | int, b: float | int) -> (float | int):
    return a + b

def subtract(a: float | int, b: float | int) -> (float | int):
    return a - b

def multiply(a: float | int, b: float | int) -> (float | int):
    return a * b

def divide(a: float | int, b: float | int) -> (float | int):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
