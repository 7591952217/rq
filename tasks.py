import time

def sample():
    time.sleep(20)  # Simulate a time-consuming task
    print("Sample task completed")
    return "Sample task completed"

def print_name(name):
    time.sleep(10)  # Simulate a time-consuming task
    print(f"Hello, {name}! Background task completed.")
    return f"Hello, {name}! Background task completed."


def add(n1, n2):
    result = n1+n2
    print("Add task completed")

    return result

def subtract(n1, n2):
    result = n1-n2
    print("Subtract task completed")

    return result