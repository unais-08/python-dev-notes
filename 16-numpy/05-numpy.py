import numpy as np

# Create two numpy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
sum_ab = a + b
print("a + b =", sum_ab)  # [5 7 9]

# Element-wise multiplication
product_ab = a * b
print("a * b =", product_ab)  # [4 10 18]

# Element-wise exponentiation
a_squared = a ** 2
print("a squared =", a_squared)  # [1 4 9]

# Square root of each element in a
sqrt_a = np.sqrt(a)
print("sqrt(a) =", sqrt_a)  # [1. 1.41421356 1.73205081]

# Sum of all elements in a
sum_a = np.sum(a)
print("sum(a) =", sum_a)  # 6

# Mean (average) of elements in a
mean_a = np.mean(a)
print("mean(a) =", mean_a)  # 2.0

# Maximum value in a
max_a = np.max(a)
print("max(a) =", max_a)  # 3
