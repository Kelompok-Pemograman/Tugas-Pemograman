import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.read_csv("C:/BAHASA/New folder/supermarket_sales - Sheet1.csv")
print(sales.info())

sales.set_index('Invoice ID', inplace = True)
sales['Date'] = pd.to_datetime(sales['Date'])
sales['Time'] = pd.to_datetime(sales['Time'])
sales['Year']= sales['Date'].dt.year
sales['Month']= sales['Date'].dt.month
sales['Quarter'] = sales['Date'].dt.quarter
sales['Hour'] = sales['Time'].dt.hour

sales['Time'] = sales['Time'].dt.strftime('%H:%M')

sales.sort_values('Date', inplace = True)

print(sales['Month'].unique())

sales['Month'].replace([1,2,3], ['Des', 'Jan', 'Feb'], inplace = True)
print(sales.head(3))

print(sales.describe())

sales.groupby('City')['Quantity'].agg(['sum','mean','median','std']).round(decimals = 2).sort_values('sum', ascending = False)

sales.groupby('Customer type')['Quantity'].agg(['sum','mean','median','std']).round(decimals = 2).sort_values('sum', ascending = False)

sales.groupby('Gender')['Quantity'].agg(['sum','mean','median','std']).round(decimals = 2).sort_values('sum', ascending = False)

sales.groupby('Product line')['Quantity'].agg(['sum','mean','median','std']).round(decimals = 2).sort_values('sum', ascending = False)

sales['Month'].value_counts().loc[['Des', 'Jan', 'Feb']]

print(sales['Hour'].value_counts().sort_index())

def rating_level(rate):
    if rate >= 7.5:
        return 'positive'
    elif rate >= 6.5:
        return 'neutral'
    else:
        return 'negative'

print(sales['Rating'].apply(rating_level).value_counts())

sales['Rating Level'] = sales['Rating'].apply(rating_level)

sns.set_theme()
sns.catplot(kind = 'count',data = sales, x ='Rating Level')

sns.catplot(kind = 'count',data = sales, x ='Rating Level', col = 'Branch')

sns.catplot(kind = 'bar', data = sales, x ='Month', y = 'Quantity', aspect = 1.2, estimator = sum, ci = None)
plt.xlabel('')
plt.title('Total Quantity by Month (Q1)')

sns.relplot(kind = 'line', data = sales, x ='Hour', y = 'Quantity', aspect = 2, hue = 'Gender', ci = False)
plt.xlabel('Hour of Day')
plt.title('Average Sales by Hour of Day (24 hrs)')
plt.ylim(0,24)

sns.relplot(kind = 'line', data = sales, x ='Hour', y = 'Quantity', aspect = 2)
plt.xlabel('Hour of Day')
plt.title('Average Sales by Hour of Day (24 hrs)')
plt.ylim(0,24)

sales_by_date = sales.groupby('Date')['Quantity'].agg(Quantity='sum').sort_index()

sales_by_date['5 Day Quantity'] = sales_by_date['Quantity'].rolling(5).sum()
sales_by_date['5 Day Quantity Average'] = sales_by_date['Quantity'].rolling(5).mean().round(decimals = 2)
sales_by_date['15 Day Quantity'] = sales_by_date['Quantity'].rolling(15).sum()
sales_by_date['15 Day Quantity Average'] = sales_by_date['Quantity'].rolling(15).mean().round(decimals = 2)

sales_by_date.tail()

sns.set_style('white')

sns.histplot(data = sales_by_date, x = 'Quantity', binwidth = 10, kde = True)
sns.despine()

sns.set_style('darkgrid')
sns.relplot(kind = 'line', data = sales_by_date, x ='Date', y = 'Quantity', aspect = 2.5)
plt.ylim(0,140)
sns.relplot(kind = 'line', data = sales_by_date, x ='Date', y = '5 Day Quantity Average', aspect = 2.5)
plt.ylim(0,140)
sns.relplot(kind = 'line', data = sales_by_date, x ='Date', y = '15 Day Quantity Average', aspect = 2.5)
plt.ylim(0,140)

sales_by_date.sort_values('Quantity', ascending = False).head(10
