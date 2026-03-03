import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'salary': [50000, 60000, 45000, 75000, 65000],
    'performance': [4.5, 4.2, 3.8, 4.9, 4.7]
}

df = pd.DataFrame(data)
print(df)

#df.drop(columns=['column_name'], inplace=True)
df.drop(columns=['performance'], inplace=True)
print(df)

#dropping multiple columns
df.drop(columns=['Age', 'salary'], inplace=True)
print(df)