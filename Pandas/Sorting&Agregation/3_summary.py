"""
df["column name"].mean()
df["column name"].sum()
df["column name"].min()
df["column name"].max()
"""

import pandas as pd

data = {
    "name":["arun","varun","karan"],
    "age":[28,34,22],
    "salary":[10000,20000,30000]
}

df = pd.DataFrame(data)
avg_salary = df['salary'].mean()
print(avg_salary)
