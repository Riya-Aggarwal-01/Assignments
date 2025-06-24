## dataframe with 2-D list or list of lists
import pandas as pd
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]
df = pd.DataFrame(data)
print(df)

#with dictionary

data_set = {'Name':["Riya","Parveen","Shivani"],
            'Age':[20,21,19]}
df1=pd.DataFrame(data_set)
print(df1)

#with list of tuples

data1 = [("Riya",21,"Jaipur"),
         ("Parveen",22,"Rewari"),
         ("Shivani",19,"Delhi")]

df2 = pd.DataFrame(data1)
print(df2)

#list of dict

data3 = [
    {'ID': 101, 'Name': 'Riya', 'Age': 21},
    {'ID': 102, 'Name': 'Bob', 'Age': 20},
    {'ID': 103, 'Name': 'Parveen', 'Age': 22}
]
df3 = pd.DataFrame(data3)
print(df3)

data4 = {'row1': {'ID': 1, 'Name': 'Riya'},
         'row2': {'ID': 2, 'Age': 27}}

df4 = pd.DataFrame(data4)
print(df4)