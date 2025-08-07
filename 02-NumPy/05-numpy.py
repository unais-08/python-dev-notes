import numpy as np

# NumPy: Basic Operations and Array Reshaping

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
a_squared = a**2
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


# Array Reshaping

# Example 1: Reshape 1D array to 2D
a = np.array([1, 2, 3, 4, 5, 6])
print("Original 1D array:")
print(a)
print("Shape:", a.shape)  # (6,)

# Reshape to 2 rows and 3 columns
b = a.reshape(2, 3)
print("\nReshaped to 2D (2 rows, 3 columns):")
print(b)
print("Shape:", b.shape)  # (2, 3)


# Example 2: Reshape 2D array to 1D
c = b.reshape(-1)  # Flatten the array
print("\nFlattened back to 1D:")
print(c)
print("Shape:", c.shape)  # (6,)


# Example 3: Reshape with automatic dimension using -1
d = a.reshape(3, -1)  # NumPy will figure out the second dimension
print("\nReshaped using -1 (3 rows, inferred columns):")
print(d)
print("Shape:", d.shape)  # (3, 2)


# Example 4: Reshape to 3D
e = np.array([1, 2, 3, 4, 5, 6, 7, 8])
f = e.reshape(2, 2, 2)  # 2 blocks, each 2x2
print("\nReshaped to 3D (2, 2, 2):")
print(f)
print("Shape:", f.shape)  # (2, 2, 2)


# Example 5: Invalid reshape (uncomment to see error)
# g = a.reshape(4, 2)  # ❌ Error: Cannot reshape array of size 6 into shape (4,2)

# Always ensure total elements before and after reshape are the same
