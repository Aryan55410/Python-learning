import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'salary': [50000, 60000, 45000, 75000, 65000],
    'performance': [4.5, 4.2, 3.8, 4.9, 4.7]
}

df = pd.DataFrame(data)
print(df)

# .loc[]
#df.loc[rows, columns]=new_value

df.loc[0, 'salary']=52000
print(df)

#increasing salary by 5%
df['salary'] = df['salary'] * 1.05
print(df)



