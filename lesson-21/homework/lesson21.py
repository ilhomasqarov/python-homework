import pandas as pd
import matplotlib.pyplot as plt
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)
# Exrcise 1
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
# Exercise 2
top_student = df1.loc[df1['Average'].idxmax()]
# Exercise 3
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
# Exercise 4
subject_averages = df1[['Math', 'English', 'Science']].mean()
subject_averages.plot(kind='bar', title='Average Grades per Subject', ylabel='Average Grade')
plt.tight_layout()
plt.show()

# DataFrame 2
data2 = {
  'Date': pd.date_range(start='2023-01-01', periods=10),
'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
# Exercise 1
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
# Exercise 2
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
# Exercise 3
df2_pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
# Exercise 4
df2.plot(x='Date', y=['Product_A', 'Product_B', 'Product_C'], title='Sales Trends Over Time')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()


# DataFrame 3
data3 = {
   'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
  'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
  'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)
# Exercise 1
avg_salary_dept = df3.groupby('Department')['Salary'].mean()
# Exercise 2 
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
# Exercise 3
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100
# Exercise 4
df3['Department'].value_counts().plot(kind='bar', title='Employees per Department')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.show()

