import pandas

df = pandas.read_csv('megaCoffee.csv')
# print(df)
print(df.shape) # (300,3) 행과 열
print(df.columns) # 열의 이름
print(df.index) # 행의 이름
print(df.head()) # 행의 5개 가져오기
print(df.tail()) # 행의 5개 뒤에서 가져오기
print(df.describe()) # 통계
print(df.sort_values(by='age'))
print(df.sort_values(by='name'))
