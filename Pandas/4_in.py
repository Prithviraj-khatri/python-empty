import pandas as pd
data = {
    "Name":["ram","shayam","ganshyam"],
    "Age":[10,20,30],
    "City":["ajmer","jaipur","bengluru"]
}

df = pd.DataFrame(data)

print("displaying the data of data set")
print(df.info())

