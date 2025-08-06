import numpy as np

# Array Attributes

# Create a 2D NumPy array with 2 rows and 3 columns
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Get the shape of the array (rows, columns)
print("Shape:", arr.shape)  # Output: (2, 3)

# Get the number of dimensions of the array
print("Number of dimensions:", arr.ndim)  # Output: 2

# Get the data type of the array elements
print("Data type:", arr.dtype)  # Output: int64 (may vary by system)

# Get the total number of elements in the array
print("Total elements:", arr.size)  # Output: 6
