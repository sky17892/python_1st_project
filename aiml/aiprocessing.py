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

data.columns = data.columns.str.strip()

print("컬럼 확인:", data.columns)

features = ['초장','엽수','엽장','엽폭','줄기굵기']
target = '품목'

data = data[features + [target]]

data = data.dropna()

X = data[features]
y = data[target]

print(X.head())
print(y.head())