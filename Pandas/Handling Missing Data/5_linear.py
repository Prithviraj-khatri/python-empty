import pandas as pd

data = {
    "Time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}

df = pd.DataFrame(data)
print("before interpolation")
print(df)

df['value']= df['value'].interpolate(method='linear')
print("after interpolation ")
print(df)