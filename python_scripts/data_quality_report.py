import pandas as pd

df = pd.read_csv('../supply_chain_data.csv')

missing_data = df.isnull().sum()

print(missing_data)

incorrect_quantity = df[df['Quantity'] < 0]

print("Incorrect Quantity:")
print(incorrect_quantity)

incorrect_dates = df[df['DeliveryDate'] < df['ShipmentDate']]

print("Incorrect Delivery Dates:")
print(incorrect_dates)

summary = df.describe()

print(summary)

with open("data_quality_report.txt", "w") as file:
    file.write("Data Quality Report\n")
    file.write(f"Missing Data:\n{missing_data}\n")
    file.write(f"Incorrect Quantity:\n{incorrect_quantity}\n")
    file.write(f"Incorrect Delivery Dates:\n{incorrect_dates}\n")
    file.write(f"\nSummary Statistics:\n{summary}")

print("Data quality report generated successfully!")
