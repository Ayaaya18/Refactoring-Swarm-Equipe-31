def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def calculate_average(numbers):
    if not numbers:
        raise ValueError("Empty list")
    return sum(numbers) / len(numbers)