# 🔁 What is a `for` loop?
# A `for` loop is used to iterate over a sequence (like a list, tuple, string, or range).

# 🧠 Syntax of `for` loop
# for variable in sequence:
#     # block of code

# ✅ Basic Example
for i in range(1, 6):
    print("Count is:", i)

# 🔄 Iterating over different data types

# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# String
for char in "hello":
    print(char)

# Tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# 🔁 Using `break` and `continue`

# Using `break`
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Using `continue`
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 🧮 Real-Life Example: Sum of first N numbers
n = 5
sum_val = 0
for i in range(1, n + 1):
    sum_val += i
print("Sum is:", sum_val)

# ✅ Using `for` with `else` block
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")

# 🧪 Practice Questions (with Solutions)

# 🔸 Q1: Print squares of numbers from 1 to 5
for i in range(1, 6):
    print(i**2)

# 🔸 Q2: Iterate through a list and print only strings
items = [1, "hello", 3.14, "world", True]
for item in items:
    if isinstance(item, str):
        print(item)

# 🔸 Q3: Print even numbers between 10 and 20
for i in range(10, 21):
    if i % 2 == 0:
        print(i)

# 🔸 Q4: Count vowels in a string
string = "programming"
vowels = "aeiou"
count = 0
for ch in string:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

# 🔸 Q5: Loop through dictionary
person = {"name": "Alice", "age": 25, "city": "Mumbai"}
for key, value in person.items():
    print(key, ":", value)
