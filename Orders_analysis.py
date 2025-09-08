#import libraries
import pandas as pd


# reading data and handling null values
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df["Ship Mode"].unique()


#rename columns names ..make them lower case and replace space with underscore
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head()


# Deriving new columns discount, sale price and profit
df['discount']=df['list_price']*df['discount_percent']/100
df['sale_price']=df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df.head()


# converting order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format='%Y-%m-%d')


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
df.head()


#load the data into sql server using append option
import sqlalchemy as sal
engine = sal.create_engine('mssql:..........')
conn=engine.connect()
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')
