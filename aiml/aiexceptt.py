import pandas as pd

df = pd.read_csv("data/2022_환경_통합v1.csv", encoding="cp949")

df["측정시간"] = pd.to_datetime(df["측정시간"])

start = df["측정시간"].min().strftime("%Y%m%d%H00")
end = df["측정시간"].max().strftime("%Y%m%d%H00")

API = "https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php"
KEY = "zeve4J6xQy6r3uCesVMuOA"

url = f"{API}?tm1={start}&tm2={end}&stn=108&disp=0&help=0&authKey={KEY}"

print(url)