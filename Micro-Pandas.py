import pandas as pd
import matplotlib.pyplot as plt

# Load the employee attrition data into a DataFrame
employee_data = pd.read_csv('employee_attrition.csv')

# Data Preprocessing
# Check for missing values
missing_values = employee_data.isnull().sum()
print("Missing Values:")
print(missing_values)

# EDA: Analyze the distribution of numerical features
numeric_features = ['Age', 'Salary', 'Satisfaction_Level', 'Performance_Rating']
employee_data[numeric_features].hist(bins=10, figsize=(12, 10))
plt.suptitle('Distribution of Numerical Features')
plt.show()

# Analyze the relationship between attrition status and other features
attrition_counts = employee_data['Attrition'].value_counts()
attrition_counts.plot(kind='bar')
plt.title('Attrition Status')
plt.xlabel('Attrition')
plt.ylabel('Count')
plt.show()

# Compare average salaries between employees who left and those who stayed
avg_salary = employee_data.groupby('Attrition')['Salary'].mean()
avg_salary.plot(kind='bar')
plt.title('Average Salary by Attrition Status')
plt.xlabel('Attrition')
plt.ylabel('Average Salary')
plt.show()

# Visualize reasons for attrition
reasons_counts = employee_data['Reasons_For_Leaving'].value_counts()
reasons_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Reasons for Attrition')
plt.ylabel('')
plt.show()
