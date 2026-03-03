import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'salary': [50000, 60000, 45000, 75000, 65000],
    'performance': [4.5, 4.2, 3.8, 4.9, 4.7]
}

df = pd.DataFrame(data)
#square brackets df["column_name"]=some_data
print(df)

df['bonus'] = df['salary'] * 0.1 
print(df)

#using insert method
df.insert(0, 'Employee ID', [101, 102, 103, 104, 105])
print(df)