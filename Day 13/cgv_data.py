import pandas

df = pandas.read_csv('cgv.csv')
print(df.index) # 몇개 행
print(df.columns) # 몇개 열
print(df.values) # 데이터 알려 주기
print(df.describe()) # 수치형 통계
print(df['snacks']) # ['해당 열'] 보여주기
print(df[['movie','drink']]) # [['해당열','해당열']] 보여주기
print(df[df['movie'] == '웡카']) # 영화 웡카 본 사람들 보여주기
print(df[df['snacks'] == '나초']) # 스낵 나초 먹은 사람들 보여주기
print(df[df['snacks'] == '나초'][df['movie'] == '웡카'])
print(df[df['age'] == 30][df['times'] == '조조'][df['movie'] == '웡카'][df['payments'] == '신용 카드'])













