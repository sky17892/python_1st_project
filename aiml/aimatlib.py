import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. 엑셀 로딩
# =========================
file_path = "data/2023년도_파프리카_생육데이터.xlsx"

df = pd.read_excel(file_path, engine='openpyxl')

# 컬럼 정리
df.columns = df.columns.astype(str).str.strip()

print("컬럼 확인:", df.columns)

# =========================
# 2. 필수 컬럼 체크
# =========================
if '조사일자' not in df.columns or '초장' not in df.columns:
    raise ValueError("❌ '조사일자', '초장' 컬럼 필요")

# =========================
# 3. 데이터 전처리
# =========================
df['조사일자'] = pd.to_datetime(df['조사일자'], errors='coerce')
df['초장'] = pd.to_numeric(df['초장'], errors='coerce')

df = df.dropna(subset=['조사일자', '초장'])

# 날짜 기준 정렬 (🔥 중요)
df = df.sort_values(by='조사일자')

# =========================
# 4. 미분 (성장속도)
# =========================
df['초장_diff'] = df['초장'].diff()
df['조사일자_diff'] = df['조사일자'].diff().dt.days

df['성장속도'] = df['초장_diff'] / df['조사일자_diff']

df = df.dropna(subset=['성장속도'])

print("🔥 미분 계산 완료")

# =========================
# 5. 그래프
# =========================
plt.figure()

plt.plot(df['조사일자'], df['초장'], label='superlong')
plt.plot(df['조사일자'], df['성장속도'], label='speeding')

plt.legend()
plt.xlabel("data")
plt.ylabel("sum")
plt.title("growth + speed")

plt.savefig("data/파프리카_성장그래프.png", dpi=300)

plt.show()