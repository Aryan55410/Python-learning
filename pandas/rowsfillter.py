import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'salary': [50000, 60000, 45000, 75000, 65000],
    'performance': [4.5, 4.2, 3.8, 4.9, 4.7]
}

df = pd.DataFrame(data)

high_salary = df[df['salary'] > 55000]
print("Employees with salary greater than 55000:")
print(high_salary) 

# filtering rows salary > 55k and age > 25
filtered_df = df[(df['salary'] > 55000) & (df['Age'] > 25)]
print("\nEmployees with salary greater than 55000 and age greater than 25:")
print(filtered_df)

# using OR condition 

filtered_or = df[(df['salary'] > 70000) | (df['performance'] > 4.5)]
print("\nEmployees with salary greater than 70000 or performance greater than 4.5:")
print(filtered_or)