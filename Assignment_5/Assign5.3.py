#ways to iterate over rows in dataframe

import pandas as pd
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]
df = pd.DataFrame(data)

print(df.loc[0])

for index, row in df.iterrows():
    print(f"Row {index}: {row[0]}, {row[1]}, {row[2]}")

# selecting rows in pandas based on condition
res = df[df[2]!=6]
print(res)

res1 = df[df[0]==1]
print(res1)

# select row using iloc

df = pd.DataFrame(data)
print(df)
print(df.iloc[0]) # in vertical form

## list from rows
print(df.iloc[0].tolist()) # in horizontal form

#limited row selection with given column
print(df.iloc[:2,:2])
print(df.iloc[:,:2])

#drop rows from df based on certain condition applied on column
res1=df.drop(df.index[1:2])
print(res1) ## deletes row 1

df2 = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Drop rows where column 'B' > 5
df2 = df2.drop(df2[df2['B']>5].index)
print(df2)

#inserting rows
df.iloc[1:3, 0] = [11, 13]
print(df)

row = pd.DataFrame([[10,11,12]])

df.loc[0.5] = [10, 11, 12]  # Use a fractional index to go between 0 and 1
df = df.sort_index().reset_index(drop=True)
print(df)