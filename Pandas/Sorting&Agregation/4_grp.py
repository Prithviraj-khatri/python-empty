import pandas as pd

data = {
    "name":["arun","varun","karan","narun","marun"],
    "age":[28,34,22,34,28],
    "salary":[50000,60000,45000,52000,48000]
}

df = pd.DataFrame(data)
grouped = df.groupby("age")["salary"].sum()
print(grouped)