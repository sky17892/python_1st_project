import pandas as pd
import glob

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

#if not dfs:
#    print("데이터가 없습니다. 폴더와 파일을 확인하세요.")
#else:
#    data = pd.concat(dfs, ignore_index=True, encoding='utf-8-sig')

data = pd.concat(dfs, ignore_index=True)

data.columns = data.columns.str.strip()

print("컬럼 확인:", data.columns)

target_items = ['딸기','완숙토마토','파프리카']
data = data[data['품목'].isin(target_items)]

features = ['일사량_외부','시간별_누적일사량','누적일사량_외부','온도_내부','상대습도_내부','토양온도']
target = '품목'

data = data[features + [target]]

data = data.dropna()

X = data[features]
y = data[target]

print(X.head())
print(y.head())