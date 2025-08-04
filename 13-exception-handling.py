#                      Exception Handling in Python
#
# An exception is an error that occurs during the execution of a program.
# Exception handling allows you to manage these errors gracefully without
# crashing the application.

# ------------------------------------------------------------------------------
# 1. The Basic try...except Block
# ------------------------------------------------------------------------------
# The 'try' block contains the code that might cause an exception.
# The 'except' block contains the code that is executed if an exception occurs
# in the 'try' block.

print("--- Basic try...except ---")
try:
    # This line will cause a ZeroDivisionError
    result = 10 / 0
    print(result)  # This line will not be reached
except ZeroDivisionError:
    print("An error occurred: Cannot divide by zero!")

# The program continues to run after the exception is handled.
print("Program continues here.")

# ------------------------------------------------------------------------------
# 2. Handling Specific Exceptions and Getting the Error Message
# ------------------------------------------------------------------------------
# You can specify the type of exception you want to catch. You can also
# use the 'as' keyword to get the exception object, which often contains
# a helpful error message.

print("\n--- Handling Specific Exceptions ---")
try:
    # This line will cause a ValueError if a non-integer is entered
    number = int(input("Enter an integer: "))
    print(f"You entered: {number}")
except ValueError as e:
    # The variable 'e' holds the exception object
    print(f"Invalid input! Error message: {e}")

# ------------------------------------------------------------------------------
# 3. Handling Multiple Specific Exceptions
# ------------------------------------------------------------------------------
# You can have multiple 'except' blocks to handle different types of exceptions.
# Python will execute the first 'except' block that matches the exception.

print("\n--- Handling Multiple Exceptions ---")
try:
    file_name = "non_existent_file.txt"
    # This will raise a FileNotFoundError
    with open(file_name, "r") as f:
        content = f.read()
    # This could raise a ValueError if content is invalid
    number = int(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except ValueError:
    print("Error: The file content is not a valid integer.")
except Exception as e:
    # A generic catch-all for any other unexpected exceptions.
    # It is good practice to catch specific exceptions first.
    print(f"An unexpected error occurred: {e}")

# ------------------------------------------------------------------------------
# 4. The try...except...else Block
# ------------------------------------------------------------------------------
# The 'else' block is optional and is executed only if the 'try' block
# completes successfully without raising any exceptions.

print("\n--- Using the else block ---")
try:
    # This will succeed if the user enters a valid number
    value = int(input("Enter a number: "))
except ValueError:
    print("That was not a valid number.")
else:
    # This code only runs if no exception occurred
    print(f"Success! The square of your number is: {value ** 2}")

# ------------------------------------------------------------------------------
# 5. The try...finally Block
# ------------------------------------------------------------------------------
# The 'finally' block is always executed, regardless of whether an exception
# occurred or was handled. It's typically used for cleanup actions, like
# closing files or network connections.

print("\n--- Using the finally block ---")
file_handle = None
try:
    file_handle = open("some_data.txt", "w")
    file_handle.write("Hello, World!")
    print("File was written to successfully.")
    # This will cause a ZeroDivisionError, but the finally block will still run.
    # result = 1 / 0
except IOError:
    print("An error occurred while writing to the file.")
finally:
    # The code in this block will always execute.
    if file_handle:
        print("Closing the file handle.")
        file_handle.close()

# ------------------------------------------------------------------------------
# 6. Raising Your Own Exceptions
# ------------------------------------------------------------------------------
# You can raise exceptions manually using the 'raise' keyword. This is useful
# for enforcing business logic or preconditions in your code.


class InvalidAgeError(Exception):
    """Custom exception for an invalid age."""

    pass


def set_age(age):
    if not isinstance(age, int) or age <= 0:
        # Raise our custom exception
        raise InvalidAgeError("Age must be a positive integer.")
    print(f"Age set to {age}")


print("\n--- Raising a custom exception ---")
try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"Caught an exception: {e}")

try:
    set_age(30)
except InvalidAgeError as e:
    print(f"Caught an exception: {e}")
