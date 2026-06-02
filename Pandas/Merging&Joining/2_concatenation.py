"""
vertically (row- wise)
horizontally (column - wise)

pd.concate ([df1,df2]),axis = 0, ignore_index = true)
"""
import pandas as pd
region1 = pd.DataFrame({
    "Customer":[1,2],
    "Name": ["ram","shyam"]
})

region2 = pd.DataFrame({
    "Customer":[3,4],
    "Name": ["gopal","raju"]
})

# concatinate Vertically
concat = pd.concat([region1,region2],axis=1,ignore_index=True)
print(concat)