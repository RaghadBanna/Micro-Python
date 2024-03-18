import pandas as pd
import matplotlib.pyplot as plt

# Load the online retail data into a DataFrame
retail_data = pd.read_csv('online_retail_data.csv')

# Data Preprocessing
# Check for missing values
missing_values = retail_data.isnull().sum()
print("Missing Values:")
print(missing_values)

# EDA: Explore the structure and characteristics of the dataset
print("First Few Rows:")
print(retail_data.head())

print("Summary Statistics:")
print(retail_data.describe())

# Data Analysis
# Calculate total sales revenue
retail_data['TotalPrice'] = retail_data['Quantity'] * retail_data['UnitPrice']
total_revenue = retail_data['TotalPrice'].sum()
print("Total Sales Revenue:", total_revenue)

# Identify top-selling products
top_products = retail_data.groupby('Description')['Quantity'].sum().nlargest(5)
print("Top Selling Products:")
print(top_products)

# Visualize sales trends over time
retail_data['InvoiceDate'] = pd.to_datetime(retail_data['InvoiceDate'])
retail_data['Month'] = retail_data['InvoiceDate'].dt.month
monthly_sales = retail_data.groupby('Month')['TotalPrice'].sum()
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
