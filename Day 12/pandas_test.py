from random import randint, choice
import pandas
from faker import Faker
fake = Faker()
nameList = []
ageList = []
coffeeLsit = []
coffee = ['아메리카노', '라떼', '디카페인', '밀크 라떼', '바닐라', '모카', '맥심']
# a = (list(fake.name() for i in range(299)))
# b = (list(random.randint(0, 69) for q in range(299)))
# c = (list(random.choice(coffee) for o in range(299)))
for i in range(300):
    nameList.append(fake.name())
    ageList.append(randint(10, 70))
    coffeeLsit.append(choice(coffee))

# x = (list(zip(a, b, c)))
# df = pandas.DataFrame(x)
# df.to_csv('리스트.avi', index=False)

data = {
    'name': nameList,
    'age': ageList,
    'coffee': coffeeLsit
}

df = pandas.DataFrame(data)
df.to_csv('megaCoffee.csv', index=False)
