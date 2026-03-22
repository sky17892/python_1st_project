import pandas as pd
import glob
import numpy as np
from sklearn.model_selection import train_test_split

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.unicode.east_asian_width', True)

excel_files = glob.glob("data/*.xlsx")
csv_files = glob.glob("data/*.csv")

dfs = []

for f in excel_files:
    try:
        dfs.append(pd.read_excel(f))
    except Exception as e:
        print(f"{f} 읽기 실패: {e}")

for f in csv_files:
    try:
        dfs.append(pd.read_csv(f, encoding='cp949'))
    except:
        try:
            dfs.append(pd.read_csv(f, encoding='utf-8-sig'))
        except Exception as e:
            print(f"{f} 읽기 실패: {e}")

if not dfs:
    print("데이터가 없습니다.")
    exit()

data = pd.concat(dfs, ignore_index=True)
data.columns = data.columns.str.strip()

target_items = ['딸기', '완숙토마토', '파프리카']
data = data[data['품목'].isin(target_items)]

features = [
    '일사량_외부',
    '시간별_누적일사량',
    '누적일사량_외부',
    '온도_내부',
    '상대습도_내부',
    '토양온도'
]

data = data[features].dropna()

print("\n총 데이터 수:", len(data))

def make_reg_target(row):
    # 가중합 방식 (연속값)
    return (
        row['온도_내부'] * 0.3 +
        row['상대습도_내부'] * 0.2 +
        row['일사량_외부'] * 0.3 +
        row['토양온도'] * 0.2
    )

data['growth_score'] = data.apply(make_reg_target, axis=1)

noise_ratio = 0.2

noise_idx = np.random.choice(
    data.index,
    size=int(len(data) * noise_ratio),
    replace=False
)

data.loc[noise_idx, 'growth_score'] += np.random.normal(0, 10, len(noise_idx))

X = data[features]
y = data['growth_score']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n🔥 X_train")
print(X_train.head())

print("\n🔥 y_train")
print(y_train.head())