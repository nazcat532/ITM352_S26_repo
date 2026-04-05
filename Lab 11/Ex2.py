# Read in a CSV file and create a dataframe
# Pivot the datafram, aggregating sales by region, with colums defined by order_type and totals
# ...existing code...
df['sales'] = df['quantity'] * df['unit_price'] # Calculate sales as quantity * unit_price

pivot_table = df.pivot_table(index='sales_region',
                             values='sales',
                             columns='order_type',
                             aggfunc=np.sum,
                             margins=True,
                             margins_name='Total Sales')

print(pivot_table)
import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None) # Show all columns in the output

df = pd.read_csv(filename, engine='pyarrow')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce') # Convert 'order_date' to datetime, coercing errors to NaT

#coerce quantity and unit_price to numeric, coercing errors to NaN
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price'] # Calculate sales as quantity * unit_price


pivot_table = df.pivot_table(df,
                             index= 'sales_region',
                             values= 'sales',
                             columns= 'order_type',
                             aggfunc=np.sum,
                             margins=True,
                             margins_name='Total Sales')

print(pivot_table)