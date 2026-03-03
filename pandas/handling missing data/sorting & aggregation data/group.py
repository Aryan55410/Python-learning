import pandas as pd

Data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 28, 30, 28],
    "salary": [50000, 60000, 45000, 70000, 55000]
}

df = pd.DataFrame(Data)

grouped = df.groupby("Age")["salary"].sum()

print(grouped)
