# ==============================================================================
#                          Python Modules: A Beginner's Guide
# ==============================================================================
# A Python module is simply a file containing Python code. It can define
# functions, classes, and variables.
# The filename is the module name with the .py extension.
# For example, a file named 'my_math_tools.py' would be a module named 'my_math_tools'.
#
# This document will simulate two files: a module file and a main script file
# that uses the module.

# ------------------------------------------------------------------------------
# Part 1: The Module File (Simulated as 'my_math_tools.py')
# ------------------------------------------------------------------------------
# Imagine this code is saved in a file named 'my_math_tools.py'.

# A simple variable
PI = 3.14159


# A function to calculate the area of a circle
def circle_area(radius):
    """Calculates the area of a circle given its radius."""
    return PI * (radius**2)


# A class definition
class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


# The special '__name__' variable is 'my_math_tools' when this file is imported.
# But when we run this file directly, it's set to '__main__'.
# This block of code is only executed if the script is run directly, not when imported.
if __name__ == "__main__":
    print("This code is running directly from 'my_math_tools.py'")
    print(f"The value of PI is {PI}")
    radius = 5
    area = circle_area(radius)
    print(f"The area of a circle with radius {radius} is {area}")


# ------------------------------------------------------------------------------
# Part 2: The Main Script (Simulated as 'main_script.py')
# ------------------------------------------------------------------------------
# Imagine this code is saved in another file, 'main_script.py', in the same directory.
# This script will now import and use the code from 'my_math_tools.py'.

# ==============================================================================
# Importing a Module
# ==============================================================================

# Method 1: Import the entire module
# This is the most common and recommended way. It keeps your code organized
# by requiring you to use the module name as a prefix.
print("--- Method 1: Importing the entire module ---")
import my_math_tools

# To use anything from the module, you must prefix it with the module name.
print(f"PI from the module is: {my_math_tools.PI}")

radius_value = 10
calculated_area = my_math_tools.circle_area(radius_value)
print(f"The area of a circle with radius {radius_value} is {calculated_area}")

calc = my_math_tools.Calculator()
sum_result = calc.add(5, 3)
print(f"5 + 3 = {sum_result}")

# Method 2: Import specific functions or variables
# This allows you to use the imported items directly without the module name prefix.
# Use this when you only need a few things from a module.
print("\n--- Method 2: Importing specific items ---")
from my_math_tools import circle_area, Calculator

# Now we can use 'circle_area' and 'Calculator' directly.
radius_value = 7
calculated_area_2 = circle_area(radius_value)
print(f"The area of a circle with radius {radius_value} is {calculated_area_2}")

calc_2 = Calculator()
product_result = calc_2.multiply(4, 6)
print(f"4 * 6 = {product_result}")

# Method 3: Importing with an alias
# This is useful for long module names or to avoid name conflicts.
print("\n--- Method 3: Importing with an alias ---")
import my_math_tools as mmt

print(f"PI from the aliased module is: {mmt.PI}")

# Method 4: The 'wildcard' import
# WARNING: This is generally considered bad practice as it imports ALL items
# from the module into your current namespace. This can lead to name conflicts
# and make your code harder to read. Use with caution.
print("\n--- Method 4: The wildcard import (use with caution!) ---")
from my_math_tools import *

# Now we can use everything from the module directly, which can be confusing.
print(f"PI directly is: {PI}")

# ==============================================================================
# Key Takeaways
# ==============================================================================
# - Modules help organize your code into separate, logical files.
# - The 'import' statement brings code from one module into another script.
# - The 'if __name__ == "__main__":' block is a useful pattern for making code
#   reusable (when imported) and runnable (when executed directly).
# - Prefer `import module_name` or `from module_name import function` over `*`.
