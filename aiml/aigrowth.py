import pandas as pd
import glob
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

excel_files = glob.glob("data/*.xlsx")
csv_files = glob.glob("data/*.csv")

dfs = []

for f in excel_files:
    try:
        df = pd.read_excel(f, engine='openpyxl')
        df.columns = df.columns.astype(str).str.strip()
        df['source_file'] = f
        dfs.append(df)
    except Exception as e:
        print(f"{f} 읽기 실패: {e}")

for f in csv_files:
    try:
        df = pd.read_csv(f, encoding='cp949')
    except:
        try:
            df = pd.read_csv(f, encoding='utf-8-sig')
        except Exception as e:
            print(f"{f} 읽기 실패: {e}")
            continue

    df.columns = df.columns.astype(str).str.strip()
    df['source_file'] = f
    dfs.append(df)

if not dfs:
    raise ValueError("데이터가 없습니다.")

data = pd.concat(dfs, ignore_index=True)

print("\n🔥 전체 데이터:", data.shape)
print("\n🔥 컬럼 목록:", data.columns.tolist())

for col in ['품목', '도', '시군']:
    if col in data.columns:
        data[col] = data[col].astype(str).str.strip()

if all(col in data.columns for col in ['품목', '도', '시군']):
    print("\n🔥 필터 전:", data.shape)

    data = data[
        (data['품목'].str.contains('파프리카', na=False)) &
        (data['도'].str.contains('강원', na=False)) &
        (data['시군'].str.contains('인제', na=False))
    ]

    print("🔥 필터 후:", data.shape)
else:
    print("\n⚠️ 필터 컬럼 없음 → 전체 데이터 사용")

features = [
    '초장', '엽수', '엽장', '엽폭',
    '줄기굵기', '화방높이', '개화마디', '착과마디'
]

missing_cols = [col for col in features if col not in data.columns]
if missing_cols:
    raise ValueError(f"❌ 필요한 컬럼 없음: {missing_cols}")

growth_df = data.dropna(subset=features)

if len(growth_df) == 0:
    raise ValueError("❌ 생육 데이터 없음")

def make_target(x):
    if x < 30:
        return 0
    elif x < 60:
        return 1
    else:
        return 2

growth_df['growth_stage'] = growth_df['초장'].apply(make_target)

X = growth_df[[
    '엽수', '엽장', '엽폭',
    '줄기굵기', '화방높이', '개화마디', '착과마디'
]]

y = growth_df['growth_stage']

print("\n🔥 X 타입 확인:\n", X.dtypes)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("\n🌲 RandomForest")
print("정확도:", accuracy_score(y_test, rf_pred))
print(classification_report(y_test, rf_pred))

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

knn_pred = knn.predict(X_test_scaled)

print("\n📍 KNN")
print("정확도:", accuracy_score(y_test, knn_pred))
print(classification_report(y_test, knn_pred, labels=[0,1,2], zero_division=0))