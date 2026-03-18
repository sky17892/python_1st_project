import pandas as pd

file_path = 'data/환경_2020.csv'
try:
    df = pd.read_csv(file_path, encoding='cp949')
except:
    df = pd.read_csv(file_path, encoding='utf-8-sig')

target_items = ['완숙토마토', '파프리카', '딸기']
df = df[df['품목'].isin(target_items)].copy()
df['측정시간'] = pd.to_datetime(df['측정시간'])
df = df.sort_values(by=['품목', '측정시간'], ascending=True).reset_index(drop=True)

accumulated_list = []
hourly_accumulated_list = []
status_list = []
prev_value = 0
total_prev_value = 0
interval = 10 / 60

for i in range(len(df)):
    row = df.iloc[i]
    current_val = row['일사량_외부']
    current_date = row['측정시간'].date()
    current_item = row['품목']

    if i > 0:
        prev_row = df.iloc[i - 1]
        if current_date != prev_row['측정시간'].date() or current_item != prev_row['품목']:
            prev_value = 0
        if current_item != prev_row['품목']:
            total_prev_value = 0

    status = ""
    if 0 < i < len(df) - 1:
        prev_r = df.iloc[i - 1]
        next_r = df.iloc[i + 1]
        if (prev_r['품목'] == current_item == next_r['품목'] and
                prev_r['측정시간'].date() == current_date == next_r['측정시간'].date()):
            if prev_r['일사량_외부'] > current_val and current_val > next_r['일사량_외부']:
                status = "이상치"

    if current_val <= 0:
        new_accumulated = 0
    else:
        new_accumulated = prev_value + (current_val * interval)

    new_hourly_accumulated = total_prev_value + (current_val * interval)

    new_accumulated = round(new_accumulated, 2)
    new_hourly_accumulated = round(new_hourly_accumulated, 2)

    accumulated_list.append(new_accumulated)
    hourly_accumulated_list.append(new_hourly_accumulated)
    status_list.append(status)

    prev_value = new_accumulated
    total_prev_value = new_hourly_accumulated

df['시간별_누적일사량'] = hourly_accumulated_list
df['누적일사량_외부'] = accumulated_list
df['비고'] = status_list

cols = df.columns.tolist()
if '시간별_누적일사량' in cols and '누적일사량_외부' in cols:
    cols.insert(cols.index('누적일사량_외부'), cols.pop(cols.index('시간별_누적일사량')))
df = df[cols]

df.to_csv('data/환경_2020_최종본.csv', index=False, encoding='utf-8-sig')

print("작업이 완료되었습니다! '시간별_누적일사량' 컬럼이 추가되었습니다.")