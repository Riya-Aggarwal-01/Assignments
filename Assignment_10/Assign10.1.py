import numpy as np
#replacing nan
arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94],[np.nan,6,45,3]])
newarr = np.nan_to_num(arr,copy=True,nan=11)
print(newarr)

#changing 3 rows and colummn
arr[[0,1,2],:]=arr[[1,2,0],:]
print(arr)
arr[:,[1,2,0]]=arr[:,[2,0,1]]
print(arr)

