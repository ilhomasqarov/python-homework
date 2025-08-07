import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
df = pd.DataFrame(data)
df.columns = df.columns.str.lower().str.replace(" ", "_")
print("Renamed Columns:\n", df.columns)

print("\nFirst 3 Rows:\n", df.head(3))


mean_age = df['age'].mean()
print("\nMean Age:", mean_age)
print("\nSelected Columns:\n", df[['first_name', 'city']])
np.random.seed(0) 
df['salary'] = np.random.randint(50000, 100000, size=len(df))
print("\nDataFrame with Salary Column:\n", df)
print("\nSummary Statistics:\n", df.describe(include='all'))


sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})


print("\nMaximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())
print("\nMinimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())
print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

# Create the DataFrame
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

expenses.set_index('Category', inplace=True)
print("\nMaximum expense per category:\n", expenses.max(axis=1))
print("\nMinimum expense per category:\n", expenses.min(axis=1))
print("\nAverage expense per category:\n", expenses.mean(axis=1))

