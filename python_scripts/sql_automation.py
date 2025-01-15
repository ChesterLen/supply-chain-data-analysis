import sqlite3
import pandas as pd
from sqlalchemy import create_engine

conn = sqlite3.connect('../supply_chain.db')


def run_sql_query(query):
    df = pd.read_sql_query(query, conn)
    return df


def get_total_revenue():
    query = 'SELECT SUM(Price * Quantity) AS TotalRevenue FROM Orders'
    return run_sql_query(query)


total_revenue_df = get_total_revenue()
print("Total Revenue:")
print(total_revenue_df)
