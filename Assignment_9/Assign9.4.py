import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(np.max(arr)) #max ele
print(np.min(arr)) #min ele
print(arr.shape) #depth,row,column

for x in np.nditer(arr): #each element
    print(x,end=" ")
print()
#specific element
print(arr[0:1,0:2,1])
print(arr[0:2,0])
print(arr[0:1,0:1,1])

arr2 = np.array([[1,2,3],[4,5,6]])
print(np.sum(arr2))

sum = 0
for row in arr2:
    for x in row:
        sum+=x

print(sum)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a+b)
print(a-b)
print(a*b)
print(np.round(a/b,2))

print(a+2)
print(b*4)