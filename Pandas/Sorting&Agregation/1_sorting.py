# sorting data
import pandas as pd

data = {
    "name":["arun","varun","karan"],
    "age":[28,34,22],
    "salary":[10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by="age",ascending=False,inplace=True)
print("sorted age by descending")
print(df)