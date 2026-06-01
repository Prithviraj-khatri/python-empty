import pandas as pd

# df = pd.read_csv(r"C:\Users\prith\Desktop\Python\Python\Pandas\sales_data_sample.csv", encoding="latin1")
# df = pd.read_excel(r"C:\Users\prith\Desktop\Python\Python\Pandas\SampleSuperstore (1).xlsx")
df = pd.read_json(r"C:\Users\prith\Desktop\Python\Python\Pandas\sample_Data.json")
print(df)