import pandas as pd

data = {
    'OrderID': [1, 2, 3],
    'CustomerName': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Quantity': [1, 2, 3],
    'OrderDate': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'ShipmentDate': ['2024-01-03', '2024-01-04', '2024-01-05'],
    'DeliveryDate': ['2024-01-06', '2024-01-05', '2024-01-07'],
    'Price': [1200.00, 800.00, 600.00]
}

df = pd.DataFrame(data)
df.to_csv('supply_chain_data.csv', index=False)
print('Dataset created successfully!')