person = {"name": "Alice", "age": 30, "city": "New York"}

# print(list(person.values()))
# print(list(person.keys()))
# The code person.update("name") is incorrect.
# The update() method expects a dictionary or iterable of key-value pairs, not a string.
# If you want to update the value of "name", use:
person["name"] = "Bob"  # Example: change name to "Bob"
# Or, to update multiple values:
person.update({"age": 25})
print(person)