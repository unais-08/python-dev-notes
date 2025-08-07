import numpy as np

"""
NumPy Indexing and Slicing Tutorial
===================================

NumPy arrays allow powerful ways to access and modify data using indexing and slicing.

1. Importing NumPy
------------------
"""

"""
2. Creating a NumPy Array
-------------------------
"""
arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

"""
3. Indexing
-----------
- Access elements by their index (zero-based).
"""
print("Element at index 0:", arr[0])  # 10
print("Element at index 3:", arr[3])  # 40

"""
4. Negative Indexing
--------------------
- Use negative indices to access elements from the end.
"""
print("Last element:", arr[-1])  # 50
print("Second last element:", arr[-2])  # 40

"""
5. Slicing
----------
- Syntax: array[start:stop:step]
- Returns a new array with selected elements.
"""
print("Elements from index 1 to 3:", arr[1:4])  # [20 30 40]
print("Elements from start to index 2:", arr[:3])  # [10 20 30]
print("Elements from index 2 to end:", arr[2:])  # [30 40 50]
print("Every second element:", arr[::2])  # [10 30 50]

"""
6. Slicing with Negative Step
-----------------------------
- Reverse the array or select elements in reverse order.
"""
print("Reversed array:", arr[::-1])  # [50 40 30 20 10]

"""
7. Indexing and Slicing in 2D Arrays
------------------------------------
"""
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D array:\n", mat)

# Access element at row 1, column 2
print("Element at (1,2):", mat[1, 2])  # 6

# Get first row
print("First row:", mat[0, :])  # [1 2 3]

# Get second column
print("Second column:", mat[:, 1])  # [2 5 8]

# Get submatrix (rows 0-1, columns 1-2)
print("Submatrix:\n", mat[0:2, 1:3])  # [[2 3], [5 6]]

"""
8. Boolean Indexing
-------------------
- Select elements based on a condition.
"""
print("Elements > 25:", arr[arr > 25])  # [30 40 50]

"""
Summary
-------
- Use indexing and slicing to efficiently access and modify NumPy arrays.
- Works for 1D and multi-dimensional arrays.
"""
