import numpy as np  # Import the NumPy library

# Array Creation

# Create a 1D NumPy array with values from 1 to 5
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Create a 3x3 array filled with zeros
print(np.zeros((3, 3)))

# Create a 3x3 array filled with ones
print(np.ones((3, 3)))

# Create a 3x3 array with random values between 0 and 1
print(np.random.rand(3, 3))

# Create a 1D array with values from 0 to 9 (step size 1)
print(np.arange(0, 10, 1))

# Create 5 evenly spaced numbers between 0 and 1 (inclusive)
print(np.linspace(0, 1, 5))  # 5 points between 0 and 1
