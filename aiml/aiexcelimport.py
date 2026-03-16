import pandas as pd
import glob

excel_files = glob.glob("data/*.xlsx")
csv_files = glob.glob("data/*.csv")

dfs = []

for f in excel_files:
    dfs.append(pd.read_excel(f))

for f in csv_files:
    dfs.append(pd.read_csv(f))

data = pd.concat(dfs, ignore_index=True)

print(data.head())
print(data.info())