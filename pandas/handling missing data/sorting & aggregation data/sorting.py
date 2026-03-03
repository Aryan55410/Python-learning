#df.sort_values(by=["Age", "salary"]), ascending=[True, False]),inplace=True
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 22, 35, 28],
    "Score": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)
print(df)

df.sort_values(by=["Age", "Score"], ascending=False, inplace=True)
print('sorted age by descending')
print(df)