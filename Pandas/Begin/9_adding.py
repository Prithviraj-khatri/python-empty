import pandas as pd

data = {
    "Name":["ram","shayam","ganshyam","dhanshyam","aditi","jagdish","raj","simram"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "PerformanceScore":[80,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

# Adding column
df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert
df.insert(0,"EmployeeID",[10,20,30,40,50,60,70,80])
print(df)