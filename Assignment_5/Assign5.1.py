## create pandas series from dictionary
import pandas as pd
data = {"a":1,"b":2,"c":"3","d":4,"e":5}
s = pd.Series(data)
print(s)

## create pandas series from lists
data_Set = ["A","B","C","D","E"]
s1 = pd.Series(data_Set)
print(s1)

## Accessing the elements of series

print(s1[0]) # single elements by index
print(s1[3])
print(s1[[0,2,3]]) ## access multiple elements
print(s1.iloc[3]) #index

s2 = pd.Series(data_Set,index=['a','b','c','d','e'])
print(s2['a'])
print(s2.loc['c'])
print(s1[1:3])
print(s2.loc['a':'d'])