# Python Sets Tutorial

# Creating a set
my_set = {1, 2, 3, 4}
print("Set:", my_set)

# Sets do not allow duplicate elements
dup_set = {1, 2, 2, 3}
print("No duplicates:", dup_set)

# Creating a set from a list
list_set = set([1, 2, 3, 2])
print("Set from list:", list_set)

# Adding elements
my_set.add(5)
print("After add:", my_set)

# Removing elements
my_set.remove(3)  # Raises KeyError if not present
print("After remove:", my_set)

my_set.discard(10)  # Does nothing if not present
print("After discard:", my_set)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Checking membership
print(2 in a)
print(5 not in a)

# Iterating over a set
for item in a:
    print("Item:", item)

# Set comprehension
squared = {x*x for x in range(5)}
print("Set comprehension:", squared)