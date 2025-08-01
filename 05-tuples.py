# Python Tuples Tutorial

# 1. Creating a tuple
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# 2. Tuples can contain different data types
mixed_tuple = (1, "hello", 3.14)
print("Mixed Tuple:", mixed_tuple)

# 3. Tuples are immutable (cannot be changed)
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

# 4. Accessing tuple elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 5. Slicing tuples
print("Slice [1:]:", my_tuple[1:])

# 6. Tuple unpacking
a, b, c = my_tuple
print("Unpacked:", a, b, c)

# 7. Single element tuple (note the comma)
single = (5,)
print("Single element tuple:", single)

# 8. Tuple methods: count() and index()
numbers = (1, 2, 2, 3, 4, 2)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))

# 9. Looping through a tuple
for item in mixed_tuple:
    print("Item:", item)

# 10. Nested tuples
nested = ((1, 2), (3, 4))
print("Nested tuple:", nested)
print("Access nested element:", nested[1][0])
