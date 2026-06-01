import pandas as pd

data = {
    "Name":["ram","shayam","ganshyam","dhanshyam","aditi","jagdish","raj","simram"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "PerformanceScore":[80,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

# single condition
high_salary = df[df['Salary']>50000]
print("employee with salary above 50000")
print(high_salary)

# multiple condition
filtered = df[(df['Age']>30) & (df['Salary']>50000)]
print(f"employee list age > 30 + salary >50000")
print(filtered)

# using or condition
filtered_or = df[(df['Age']>35) | (df['PerformanceScore']>90)]
print(f"employee list age > 30 or PerformanceScore > 90")
print(filtered_or)
