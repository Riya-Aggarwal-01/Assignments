import numpy as np
#solve
# x-2y+3z=9
# -x+3y-z=-6
# 2x-5y+5z=17

A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])

B = np.array([9, -6, 17])
res = np.linalg.solve(A,B)
print(res)

#using inverse
A_1=np.linalg.inv(A)
res = np.dot(A_1,B)
print(res)