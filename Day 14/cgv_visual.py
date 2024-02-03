import pandas
import matplotlib.pyplot as plt

# x = [i for i in range(10)]
# y = [i for i in range(10,20)]
# plt.plot(x,y)
# plt.show()
df = pandas.read_csv('cgv.csv')
movie_groupby_time = df.groupby('times')['movie'].value_counts()
night_movies = movie_groupby_time['심야']
print(df)

plt.rcParams['font.family'] = 'Malgun Gothic' #한글 폰트 나오도록 설정
#night_movies.plot.pie(autopct = '%1.1f%%') # 숫자 비율을 소수점 1까지 보여주기
#plt.title('심야 영화 파이그래프')
#plt.show()

movie_groupby_snacks = df.groupby('movie')['snacks'].value_counts()
your_name = movie_groupby_snacks['너의 이름은']
your_name.plot.pie(autopct = '%1.1f%%')
plt.title('너의 이름은 그래프')
plt.show()






