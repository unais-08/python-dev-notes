# Python Introduction

# Basic Data Types
integer_var = 10           # int
float_var = 3.14           # float
string_var = "Hello"       # str
bool_var = True            # bool

print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", bool_var)

# Operators
a = 5
b = 2

print("\nOperators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Type Casting
num_str = "123"
num_int = int(num_str)     # str to int
num_float = float(num_str) # str to float

print("\nType Casting:")
print("String to int:", num_int)
print("String to float:", num_float)
print("Int to string:", str(num_int))

# User Input
user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))

print("Hello,", user_name + "!")
print("You are", user_age, "years old.")