import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'salary': [50000, 60000, 45000, 75000, 65000],
    'performance': [4.5, 4.2, 3.8, 4.9, 4.7]
}

df = pd.DataFrame(data)
# display the dataframe 
print("sample data frame:")
print(df)
print("names (single column return series)")
name = df['Name']
print(name)

#selectimg multiple columns
subset = df[['Name', 'salary']]
print("\n subset with name aand salary columns:")
print(subset)
