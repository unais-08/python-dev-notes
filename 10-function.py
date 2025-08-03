# Python Functions Tutorial

# 1. What is a function?
# A function is a block of code that performs a specific task.
# It helps organize code, reuse logic, and improve readability.


# 2. Defining a function
def greet():
    print("Hello, welcome to Python functions!")


# 3. Calling a function
greet()  # Output: Hello, welcome to Python functions!


# 4. Function with parameters
def add(a, b):
    return a + b


result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8


# 5. Function with default parameters
def power(base, exponent=2):
    return base**exponent


print(power(3))  # Output: 9 (default exponent 2)
print(power(2, 3))  # Output: 8


# 6. Function with variable number of arguments (*args)
def print_numbers(*args):
    for num in args:
        print(num)


print_numbers(1, 2, 3, 4)  # Output: 1 2 3 4


# 7. Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25)  # Output: name: Alice, age: 25


# 8. Returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)


minimum, maximum = min_max([2, 8, 1, 6])
print("Min:", minimum, "Max:", maximum)  # Output: Min: 1 Max: 8


# 9. Nested functions
def outer():
    def inner():
        print("This is the inner function.")

    print("This is the outer function.")
    inner()


outer()
# Output:
# This is the outer function.
# This is the inner function.

# 10. Lambda (anonymous) functions
square = lambda x: x * x
print(square(5))  # Output: 25


# 11. Docstrings (function documentation)
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b


print(multiply.__doc__)  # Output: Multiplies two numbers and returns the result.

# 12. Scope: Local and Global variables
x = 10  # Global variable


def show_scope():
    x = 5  # Local variable
    print("Local x:", x)


show_scope()  # Output: Local x: 5
print("Global x:", x)  # Output: Global x: 10


# 13. Recursive functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120

# Functions are powerful tools in Python for organizing and reusing code!
