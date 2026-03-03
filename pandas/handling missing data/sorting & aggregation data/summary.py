"""
    df["column name"].mean()
    df["column name"].sum()
    df["column name"].min()
    df["column name"].max() 
"""
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 22, 35, 28],
    "salary": [50000, 60000, 45000, 70000, 55000]
}
df = pd.DataFrame(data)
print(df)  


avg_salary = df["salary"].mean()
print(avg_salary)