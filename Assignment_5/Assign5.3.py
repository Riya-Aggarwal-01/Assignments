#ways to iterate over rows in dataframe

import pandas as pd
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]
df = pd.DataFrame(data)
print(df)
print(df.iloc[0]) # in vertical form
print(df.iloc[0].tolist()) # in horizontal form

# selecting rows in pandas based on condition
res = df[df[2]!=6]
print(res)

res1 = df[df[0]==1]
print(res1)

