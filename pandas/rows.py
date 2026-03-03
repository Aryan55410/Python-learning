#head() tail()
import pandas as pd
df = pd.read_json("sample_Data.json")

print('display 10 rows of first ')
print(df.head(10))

print('display 10 rows of last ')
print(df.tail(10))
