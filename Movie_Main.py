import pandas as pd
import matplotlib.pyplot as plt

# Load the book sales data into a DataFrame
book_sales_data = pd.read_csv('book_sales_data.csv')

# Data Preprocessing
# Check for missing values
missing_values = book_sales_data.isnull().sum()
print("Missing Values:")
print(missing_values)

# EDA: Explore the structure and characteristics of the dataset
print("First Few Rows:")
print(book_sales_data.head())

print("Summary Statistics:")
print(book_sales_data.describe())

# Data Analysis
# Identify top-selling genres and bestselling authors
top_genres = book_sales_data['Genre'].value_counts().nlargest(5)
print("Top Selling Genres:")
print(top_genres)

top_authors = book_sales_data['Author'].value_counts().nlargest(5)
print("Bestselling Authors:")
print(top_authors)

# Visualize sales trends over time
book_sales_data['Publication_Date'] = pd.to_datetime(book_sales_data['Publication_Date'])
book_sales_data['Year'] = book_sales_data['Publication_Date'].dt.year
yearly_sales = book_sales_data.groupby('Year')['Sales_Quantity'].sum()
yearly_sales.plot(kind='line', marker='o')
plt.title('Yearly Book Sales Trends')
plt.xlabel('Year')
plt.ylabel('Sales Quantity')
plt.show()
