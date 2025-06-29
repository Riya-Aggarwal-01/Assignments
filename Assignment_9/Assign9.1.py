import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([[5,6,7,8],[9,10,11,12]])

res = np.concatenate((arr2,arr1.reshape(2,2)),axis=1) # column
print(res)

res = np.concatenate((arr2,arr1.reshape(1,4))) # row
print(res)