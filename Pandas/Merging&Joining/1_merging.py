import pandas as pd

#customer dataframe

customer = pd.DataFrame({
    "CustomerID": [1,2,3],
    "Name":["Ramesh","Suresh","kalpesh"]
})

#order dataframe
order = pd.DataFrame({
    "CustomerID": [1,2,4],
    "Orderamount":[240,450,350]
})

# merge
df_merged = pd.merge(customer,order,on="CustomerID",how="inner")
print(df_merged)