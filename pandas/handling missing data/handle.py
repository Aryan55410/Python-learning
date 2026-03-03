#dropna()
import pandas as pd

data = {
    'Name': ['Alice', None, 'Charlie', 'David', 'Eva'],
    'Age': [24, None, 22, 32, 29],
    'salary': [50000, None, 45000, 75000, 65000],
    'performance': [4.5, None, 3.8, 4.9, 4.7]
}

df = pd.DataFrame(data)
print(df)

df.dropna(inplace=True) 
print(df) 