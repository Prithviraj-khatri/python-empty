import pandas as pd

data = {
    "Name":["ram",None,"ganshyam","dhanshyam","aditi","jagdish","raj","simram"],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "PerformanceScore":[80,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)
 # linear, polunomial, time

df.interpolate(method="linear",axis=0,inplace=True)