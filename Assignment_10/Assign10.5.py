import numpy as np
a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([[7, 8, 9], [10, 11, 12]])

a3 = np.concatenate((a1, a2), axis=0)
print(a3)

flat = a3.flatten()
print(np.mean(flat))
print(np.median(flat))

