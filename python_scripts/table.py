import sqlite3
import pandas as pd


conn = sqlite3.connect('../supply_chain.db')

df = pd.read_csv('../supply_chain_data.csv')

df.to_sql('Orders', conn, if_exists='replace', index=False)

print("Data imported into SQLite successfully!")

conn.commit()
conn.close()