import pandas as pd
import glob

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
else:
    data = pd.concat(dfs, ignore_index=True)
    data.columns = data.columns.str.strip()

    target_items = ['딸기', '완숙토마토', '파프리카']
    data = data[data['품목'].isin(target_items)]

    features = ['일사량_외부', '시간별_누적일사량', '누적일사량_외부', '온도_내부', '상대습도_내부', '토양온도', '비고']
    target = '품목'

    data = data[features + [target]].dropna()

    X = data[features]
    y = data[target]

    print("\n" + "=" * 100)
    print("학습 데이터 (X) 전체 출력")
    print("-" * 100)
    print(X)
    print(f"\n총 행 개수: {len(X)}")

    print("\n" + "=" * 100)
    print("타겟 데이터 (y) 전체 출력")
    print("-" * 100)
    print(y)
    print(f"\n총 행 개수: {len(y)}")
    print("=" * 100)