import numpy as np

arr = np.array([[1, -2, 3], [-4, 5, -6]])

arr[arr < 0] = 0  # Replace negatives with 0

print(arr)

