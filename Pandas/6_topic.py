"""
1 - how big is your data set
2 - what are the names of column
"""
import pandas as pd

data = {
    "Name":["ram","shayam","ganshyam","dhanshyam","aditi","jagdish","raj","simram"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "PerfomanceScore":[80,90,78,82,88,95,80,89]
}

df = pd.DataFrame(data)
print("sample dataframe")
print(df)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')
