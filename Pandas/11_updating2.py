import pandas as pd

data = {
    "Name":["ram","shayam","ganshyam","dhanshyam","aditi","jagdish","raj","simram"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "PerformanceScore":[80,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

# increasing salary by 5%
df['Salary'] = df["Salary"] * 1.05
print(df)