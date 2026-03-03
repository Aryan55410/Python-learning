#pd.merge(df1, df2, on="column_name", how="type_of_join")
import pandas as pd

#customers DataFrame
df_customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "customer_name": ["Alice", "Bob", "Charlie", "David"]
})

#orders DataFrame
df_orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 2, 4],
    "amount": [250, 150, 300, 400]
})

#merge
df_merged = pd.merge(df_customers, df_orders, on="customer_id", how="inner")
print('inner join')
print(df_merged)


#inner
#outer join
#merge
#right join
#left join
