import pandas
# group_by
df = pandas.read_csv('cgv.csv')
# group_by_snack = df.groupby('snacks').value_counts()
# print(group_by_snack)
# group_by_movie = df.groupby('movie')
# wonka = group_by_movie.get_group('웡카')
# print(wonka)
# group_by_snack = df.groupby('snacks')
# payments_by_snack = group_by_snack['payments'].value_counts()
# print(payments_by_snack)

# group_by_times = df.groupby('times')
# payments_by_times = group_by_times['payments'].value_counts()
# print(payments_by_times)]

# apply
def WonkaEvent(row):
    if row['movie'] == '웡카' and row['snacks'] == '카라멜':
        return '이벤트 대상 ❤'
    else:
        return '아님 💔'

def ElderEvent(row):
    if row['age'] == 50 and row['times'] == '심야':
        return '이벤트 대상 ❤'
    else:
        return '아님 💔'

df['ElderEvent'] = df.apply(ElderEvent, axis=1)
df['WonkaEvent'] = df.apply(WonkaEvent, axis=1)

print(df[df['ElderEvent'] == '이벤트 대상 ❤'][df['WonkaEvent'] == '이벤트 대상 ❤'])










