import pandas
import matplotlib.pyplot as plt

#30대에서 시민덕희 본사람중 음료 비율
df = pandas.read_csv('cgv.csv')
age_30_civil_df = df[df['age']==30][df['movie']=='시민 덕희']
drink = age_30_civil_df['drink'].value_counts()

plt.rcParams['font.family'] = 'Malgun Gothic' #한글 폰트 나오도록 설정
# pie그래프(일변량)
# drink.plot.pie(autopct = '%1.1f%%') # 숫자 비율을 소수점 1까지 보여주기

# bar 그래프(이변량)
drink.plot(kind='bar')
plt.title('음료와 30대가 시민 덕희 본 사람의 관계')
plt.show()

# age_group = df.groupby('age').value_counts()
# print(age_group.loc[30]) #.loc
#
# movie_group = df.groupby('movie').value_counts()
# print(movie_group.loc['시민 덕희']) #.loc

