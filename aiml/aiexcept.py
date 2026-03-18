import pandas as pd

file_path = 'data/환경_2020.csv'
try:
    df = pd.read_csv(file_path, encoding='cp949')
except:
    df = pd.read_csv(file_path, encoding='utf-8-sig')

target_items = ['완숙토마토','파프리카','딸기']
df = df[df['품목'].isin(target_items)].copy()
df['측정시간'] = pd.to_datetime(df['측정시간'])
df = df.sort_values(by=['품목', '측정시간'], ascending=True).reset_index(drop=True)

accumulated_list = []
status_list = []
prev_value = 0
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

    status = ""
    if 0 < i < len(df) - 1:
        prev_r = df.iloc[i - 1]
        next_r = df.iloc[i + 1]

        if (prev_r['품목'] == current_item == next_r['품목'] and
                prev_r['측정시간'].date() == current_date == next_r['측정시간'].date()):

            v_prev = prev_r['누적일사량_외부']
            v_next = next_r['누적일사량_외부']

            if v_prev > current_val and current_val > v_next:
                status = "이상치"

    if current_val <= 0:
        new_accumulated = 0
    else:
        new_accumulated = prev_value + (current_val * interval)

    new_accumulated = round(new_accumulated, 2)

    accumulated_list.append(new_accumulated)
    status_list.append(status)
    prev_value = new_accumulated

df['누적일사량_외부'] = accumulated_list
df['비고'] = status_list

df.to_csv('data/환경_2020_최종본.csv', index=False, encoding='utf-8-sig')

print("이상치 판별 및 누적 계산이 완료되었습니다!")