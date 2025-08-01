# Python Conditionals

# 1. Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# 3. if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")

# 4. Nested if statements
age = 20
if age >= 18:
    if age < 21:
        print("You are an adult but not 21 yet.")
    else:
        print("You are 21 or older.")
else:
    print("You are a minor.")

# 5. Using logical operators
a = 7
b = 12
if a > 5 and b > 10:
    print("Both conditions are True")

if a < 5 or b > 10:
    print("At least one condition is True")

if not (a < 5):
    print("a is not less than 5")

# 6. Ternary conditional operator
num = 4
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

# 7. Checking for empty values
my_list = []
if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")


# University Grade Assignment Program

# Take input
marks = float(input("Enter your marks out of 100: "))

# Check for valid input
if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
else:
    # Grade assignment
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B+"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"  # Fail

    # Output
    if grade == "F":
        print("Grade: F (Fail)")
    else:
        print(f"Grade: {grade}")
