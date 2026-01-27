# Utility module for basic calculator operations

def add(a, b):
    return a + b         # returns sum

def subtract(a, b):
    return a - b         # returns difference

def multiply(a, b):
    return a * b        # returns product

def divide(a, b):
    try:
        return a / b    # Return the division 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
