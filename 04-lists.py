# Python List Tutorial

# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# 2. Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Modifying elements
fruits[1] = "blueberry"
print("Modified fruits:", fruits)

# 4. Adding elements
fruits.append("orange")
print("After append:", fruits)

fruits.insert(1, "mango")
print("After insert at index 1:", fruits)

# 5. Removing elements
fruits.remove("cherry")
print("After removing 'cherry':", fruits)

popped = fruits.pop()
print("Popped element:", popped)
print("After pop:", fruits)

# 6. List length
print("Number of fruits:", len(fruits))

# 7. Iterating through a list
print("All fruits:")
for fruit in fruits:
    print(fruit)

# 8. List slicing
print("First two fruits:", fruits[:2])

# 9. List comprehension
squared = [x**2 for x in range(5)]
print("Squared numbers:", squared)

# 10. Checking membership
if "apple" in fruits:
    print("Apple is in the list.")

# 11. Sorting a list
numbers = [3, 1, 4, 2]
numbers.sort()
print("Sorted numbers:", numbers)

numbers.sort(reverse=True)
print("Sorted numbers in reverse:", numbers)

# 12. Copying a list
fruits_copy = fruits.copy()
print("Copied fruits:", fruits_copy)