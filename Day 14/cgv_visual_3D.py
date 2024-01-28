import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv('cgv.csv')
# 1. 시간과 음료를 그룸핑
grouping = df.groupby(['movie', 'popcorn'])
# 2. 크기 계산
sizeGroup = grouping.size()
# 3. 테이블화
table = sizeGroup.unstack(fill_value=0)

plt.rcParams['font.family'] = 'Malgun Gothic'
sns.heatmap(table, cmap='coolwarm') # 테이블데이터 히트맵화
plt.xticks(rotation=45) # x 축 글씨 45도 돌리기
plt.yticks(rotation=45) # x 축 글씨 45도 돌리기
plt.show() # 보여주기








