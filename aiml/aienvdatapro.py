import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

base_path = "/Users/sky88/OneDrive/바탕 화면/python_1st_document/aiml/data"
# 전체 파일 리스트로 적용 (문제가 된 2021년 포함)
env_files = ['전처리_환경_2018.csv', '전처리_환경_2019.csv', '전처리_환경_2020.csv', '전처리_환경_2021.csv', '전처리_환경_2022.csv']

# 컬럼명 설정
date_col = '날짜'
solar_col = '최대 : 일일누적일사량'
in_temp_col, in_hum_col = '평균 : 온도_내부', '평균 : 상대습도_내부'
soil_temp_col, co2_col = '평균 : 토양온도', '평균 : 잔존CO2'
farm_keys = ['도', '시군', '농가명', '작기']

print("🚀 데이터 100% 보존 모드로 전처리를 시작합니다.")
print("-" * 65)

for file_name in env_files:
    input_path = os.path.join(base_path, file_name)
    if not os.path.exists(input_path): continue
    
    # 1. 원본 데이터 로드
    df = pd.read_csv(input_path, encoding='utf-8-sig')
    original_count = len(df)
    
    # 2. 타입 변환 (행 삭제 절대 금지)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    for col in [solar_col, in_temp_col, in_hum_col, soil_temp_col, co2_col]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # --- [전략 1] 일사량: 지역(도+시군) 평균 ---
    if solar_col in df.columns:
        # 동일 날짜, 도, 시군 내의 평균값 계산
        solar_means = df.groupby([date_col, '도', '시군'])[solar_col].transform('mean')
        df[solar_col] = df[solar_col].fillna(solar_means)
        df[solar_col] = df[solar_col].round(0).astype('Int64')

    # --- [전략 2] 토양온도: 상관분석 예측 (R² >= 0.4) ---
    if all(c in df.columns for c in [soil_temp_col, in_temp_col, in_hum_col]):
        train_tmp = df.dropna(subset=[soil_temp_col, in_temp_col, in_hum_col])
        if len(train_tmp) > 100:
            features = [in_temp_col, in_hum_col]
            model = LinearRegression().fit(train_tmp[features], train_tmp[soil_temp_col])
            r2 = r2_score(train_tmp[soil_temp_col], model.predict(train_tmp[features]))
            
            if r2 >= 0.4:
                mask = df[soil_temp_col].isnull() & df[features].notnull().all(axis=1)
                if mask.any():
                    df.loc[mask, soil_temp_col] = np.round(model.predict(df.loc[mask, features]), 2)
                    print(f"📂 {file_name}: 토양온도 {mask.sum()}건 예측 (R²: {r2:.2f})")
            else:
                print(f"📂 {file_name}: 토양온도 정확도 낮음(R²: {r2:.2f}) -> 빈값 유지")

    # --- [전략 3] CO2: 시계열 보간 ---
    if co2_col in df.columns:
        # 시계열 보간을 위해 정렬 후 인덱스 재설정
        df = df.sort_values(by=farm_keys + [date_col]).reset_index(drop=True)
        # 농가별/작기별 내부 빈값만 선형으로 연결
        df[co2_col] = df.groupby(farm_keys)[co2_col].transform(lambda x: x.interpolate(method='linear', limit_area='inside'))

    # 3. 결과 저장 및 검증
    output_name = file_name.replace('.csv', '_결측치완료.csv')
    df.to_csv(os.path.join(base_path, output_name), index=False, encoding='utf-8-sig')
    
    print(f"   ㄴ 최종 행 수: {len(df)} (손실: {original_count - len(df)}행)")

print("-" * 65)
print("✨ 모든 연도의 데이터 전처리가 안전하게 완료되었습니다!")