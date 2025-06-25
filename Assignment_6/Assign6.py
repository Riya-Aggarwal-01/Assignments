import pandas as pd

#convert series of date strings to time series

date = ["2025-06-25","2025-06-24","2025-06-23","2025-06-22"]
s = pd.Series(date)
s = pd.to_datetime(s)
print(s)

#perform inner merge on common column
df1 = pd.DataFrame({'id':[1,2,3,4],
                    'Name':['A1','A2','A3','A4'],
                    'subject':['sub2','sub3','sub4','sub1'],
                    'marks':[40,50,60,70]},
                   index = [1,2,3,4])

df2 = pd.DataFrame({'id':[3,4,5,6],
                     'Name':['B1','B2','B3','B4'],
                    'subject':['sub1','sub3','sub2','sub4'],
                    'marks':[70,60,70,80]},
                     index = [1,2,3,4])

df = df1.merge(df2,on=['id']) # automatically do inner
print(df)

#perform left join on column ID
df3 = df1.merge(df2,how='left',on='id')
print(df3)

## in left join df1 will print its full table and df2 will have only that value which has column id as commnon
## rest are NaN


#right join
df3 = pd.merge(df1,df2,how='right',on='id')
print(df3)

#index-based join
df3 = df1.join(df2,lsuffix='_df1',rsuffix='_df2')
print(df3)

#merging with multiple keys
df3 = pd.merge(df1,df2,how='right',on=['marks','subject'])
print(df3)

# create three dataframe vertically concat 2 of them

df1 = pd.DataFrame({
    'id': [1, 2],
    'name': ['A1', 'A2'],
    'marks': [80, 85]
})
df2 = pd.DataFrame({
    'id': [3, 4],
    'name': ['A3', 'A4'],
    'marks': [90, 75]
})
df3 = pd.DataFrame({
    'id': [2, 3, 4, 5],
    'subject': ['Math', 'Science', 'English', 'History']
})
res = pd.concat([df1,df2],keys=['a','b'])
print(res)
res1 = res.merge(df3,on='id')
print(res1)

# primary difference on join and merge
#merge = join on column(default)
#join = join on index(default)