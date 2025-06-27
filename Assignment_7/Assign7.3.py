import pandas as pd
df = pd.read_csv('products-100.csv')

print(df.head(8))

df = df.dropna(subset=['Name', 'Price', 'Stock']) #droping rows which has missing these values
print(df)

df['Total Value'] = df['Price'] * df['Stock'] #adding new columns
expensive = df.sort_values(by='Price', ascending=False).head(5)  #5 most expensive products
brand_value = df.groupby('Brand')['Total Value'].sum().sort_values(ascending=False)

print(expensive[['Name', 'Brand', 'Price']]) # printing only name product and price of top 5
print(brand_value)

avg_price = df.groupby('Category')['Price'].mean().sort_values(ascending=False) #avg value by category
print(avg_price)

count = df['Availability'].value_counts()
print(count) #status count
