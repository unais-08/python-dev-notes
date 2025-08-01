# 🔁 What is a `while` loop?
# A `while` loop repeatedly executes a block of code as long as a condition is True.


# ✅ Basic Example
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# ⚠️ Infinite Loop Example (Use with caution)
# while True:
#     print("This will run forever! Use Ctrl+C to stop.")

# 🔄 Using `break` and `continue`

# Using `break`
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# Using `continue`
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 🧮 Real-Life Example: Sum of N numbers
n = 5
sum_val = 0
i = 1
while i <= n:
    sum_val += i
    i += 1
print("Sum is:", sum_val)

# ✅ Optional: `while` with `else` block
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished successfully!")

# 🧪 Practice Questions (with Solutions)

# 🔸 Q1: Print numbers from 10 to 1 using `while`
i = 10
while i >= 1:
    print(i)
    i -= 1

# 🔸 Q2: Print even numbers from 1 to 20
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 🔸 Q3: Find factorial of a number
n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial is:", fact)

# 🔸 Q4: Take input until user enters "exit"
# while True:
#     user_input = input("Type something (or 'exit' to quit): ")
#     if user_input.lower() == "exit":
#         print("Exiting loop...")
#         break
#     print("You typed:", user_input)

# 🔸 Q5: Sum of digits of a number
num = 1234
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10
print("Sum of digits:", sum_digits)
