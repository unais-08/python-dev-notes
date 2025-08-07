import numpy as np

# Basic of NumPy

print("NumPy version:", np.__version__)

# Create arrays of different dimensions
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Print arrays
print("\n1D Array:", arr1d)
print("2D Array:\n", arr2d)
print("3D Array:\n", arr3d)

# Print number of dimensions
print("\nNumber of dimensions:")
print("arr1d:", np.ndim(arr1d))
print("arr2d:", np.ndim(arr2d))
print("arr3d:", np.ndim(arr3d))

# Print shapes
print("\nShapes:")
print("arr1d:", np.shape(arr1d))
print("arr2d:", np.shape(arr2d))
print("arr3d:", np.shape(arr3d))

number = str(arr3d[1, 1, 0]) + str(arr3d[1, 1, 1]) + str(arr3d[1, 0, 1])
# print(arr3d[0,0,3])
print(number)
