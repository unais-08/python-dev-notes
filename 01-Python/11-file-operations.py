# --- Python File I/O: A Comprehensive Guide ---

import os  # The 'os' module is useful for interacting with the operating system,

# like checking if a file exists or getting its path.

# ====================================================================
# Part 1: Writing to a file (using 'w' mode)
# 'w' stands for 'write'. If the file exists, it will be overwritten.
# If it doesn't exist, a new one will be created.

print("--- Part 1: Writing to a file ('w' mode) ---")
file_name_write = "daily_log.txt"

# The 'with open(...) as file:' statement is the recommended way to handle files.
# It ensures that the file is automatically closed, even if errors occur.
try:
    with open(file_name_write, "w") as f:
        # The 'write()' method writes a string to the file.
        # We need to manually add newline characters '\n' for line breaks.
        f.write("Log Entry: Application started successfully.\n")
        f.write("Log Entry: User 'Alice' logged in.\n")
        f.write("Log Entry: Data processed for today.\n")
        print(
            f"Successfully wrote to '{file_name_write}' in 'w' mode (overwriting existing content)."
        )
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")

print("-" * 50)

# ====================================================================
# Part 2: Appending to a file (using 'a' mode)
# 'a' stands for 'append'. This mode adds content to the end of the file
# without overwriting the existing data.

print("--- Part 2: Appending to a file ('a' mode) ---")
try:
    with open(file_name_write, "a") as f:
        # Now, we'll append a new log entry.
        f.write("Log Entry: User 'Bob' logged in.\n")
        f.write("Log Entry: Application shut down gracefully.\n")
        print(f"Successfully appended to '{file_name_write}' in 'a' mode.")
except IOError as e:
    print(f"An error occurred while appending to the file: {e}")

print("-" * 50)

# ====================================================================
# Part 3: Reading from a file (using 'r' mode)
# 'r' stands for 'read'. This is the default mode.
# The file pointer starts at the beginning of the file.

print("--- Part 3: Reading from a file ('r' mode) ---")
try:
    with open(file_name_write, "r") as f:
        # The 'read()' method reads the entire content of the file into a single string.
        file_content = f.read()
        print("Reading the entire file content using f.read():")
        print(file_content)

    print("\nReading line by line using a for loop:")
    with open(file_name_write, "r") as f:
        # Iterating over the file object directly is memory efficient
        # and is the most common way to process large files line by line.
        for line in f:
            print(
                f"Line: {line.strip()}"
            )  # .strip() removes leading/trailing whitespace, including the newline character

    print("\nReading all lines into a list using f.readlines():")
    with open(file_name_write, "r") as f:
        # The 'readlines()' method reads all lines and returns them as a list of strings.
        # Each string in the list includes the newline character.
        lines_list = f.readlines()
        print(lines_list)
        # You can then process this list
        print("\nProcessing the list of lines:")
        for i, line in enumerate(lines_list):
            print(f"Line {i+1}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{file_name_write}' was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")

print("-" * 50)

# ====================================================================
# Part 4: A real-world example: Managing a list of users in a CSV-like file
# This example combines writing and reading in a more practical scenario.

print("--- Part 4: Real-world example: Managing user data ---")
user_file = "users.csv"
user_data = [
    "John Doe,john.doe@example.com,28\n",
    "Jane Smith,jane.smith@example.com,34\n",
    "Peter Jones,peter.jones@example.com,45\n",
]

# Writing the initial user data to a new file
try:
    with open(user_file, "w") as f:
        f.writelines(user_data)  # 'writelines()' writes a list of strings to the file.
        print(f"Successfully created and wrote user data to '{user_file}'.")
except IOError as e:
    print(f"An error occurred while writing user data: {e}")

# Reading and parsing the user data
try:
    print(f"\nReading and processing data from '{user_file}':")
    with open(user_file, "r") as f:
        for i, line in enumerate(f):
            # We use .strip() to remove the newline at the end of the line
            # and .split(',') to separate the fields by the comma.
            name, email, age = line.strip().split(",")
            print(f"User {i+1}: Name={name}, Email={email}, Age={age}")
except FileNotFoundError:
    print(f"Error: The file '{user_file}' was not found.")
except IOError as e:
    print(f"An error occurred while reading user data: {e}")

# Cleaning up the created files
print("\nCleaning up created files...")
os.remove(file_name_write)
os.remove(user_file)
print("Files deleted.")
print("-" * 50)

# ====================================================================
# Part 5: Other important file modes
# 'x' - Exclusive creation: creates a new file, but raises an error if it already exists.
# This is great for preventing accidental overwrites.

print("--- Part 5: Other file modes ('x' mode) ---")
new_file = "new_data.txt"

# First, let's create the file. This will succeed.
try:
    with open(new_file, "x") as f:
        f.write("This is a brand new file.")
        print(f"Successfully created '{new_file}' using 'x' mode.")
except FileExistsError:
    print(f"Error: The file '{new_file}' already exists. Cannot create.")

# Now, let's try to create it again. This will fail and raise a FileExistsError.
try:
    with open(new_file, "x") as f:
        f.write("This will never be written.")
except FileExistsError:
    print(
        f"\nAttempted to create '{new_file}' again. As expected, a FileExistsError was raised."
    )

# Cleaning up
os.remove(new_file)
