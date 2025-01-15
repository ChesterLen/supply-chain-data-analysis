import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('supply_chain.db')

df = pd.read_sql_query('SELECT * FROM Orders', conn)

st.title("Supply Chain Data Dashboard")

st.write("Data Preview", df.head())

total_revenue = df['Price'].sum()
st.write(f"Total Revenue: ${total_revenue:.2f}")

df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'])
df['ShipmentDate'] = pd.to_datetime(df['ShipmentDate'])
df['DeliveryTime'] = (df['DeliveryDate'] - df['ShipmentDate']).dt.days
avg_delivery_time = df['DeliveryTime'].mean()
st.write(f"Average Delivery Time: {avg_delivery_time:.2f} days")

total_revenue_by_product = df.groupby('Product')['Price'].sum()
st.bar_chart(total_revenue_by_product)
