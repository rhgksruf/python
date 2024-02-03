import pandas
from faker import Faker
import random

fake = Faker('ko_KR')
age = [20, 30, 40, 50]
agePer = [50, 30, 20, 10]
gender = ['남', '여']
genderPer = [20, 80]
item = ['바디 워시', '선크림', '스킨', '로션', '샴푸', '스낵', '향수', '에어 제품']
times = ['아침', '점심', '저녁', '밤']

olive_young = {
    'name': [fake.name() for i in range(100)],
    'age': [random.choices(age, weights=agePer, k=1)[0] for x in range(100)],
    'gender': [random.choices(gender, weights=genderPer, k=1)[0] for b in range(100)],
    'itme': [random.choice(item) for c in range(100)],
    'times': [random.choice(times) for j in range(100)]
}
a = pandas.DataFrame(olive_young)
a.to_csv('olive_young.csv', encoding='utf-8-sig', index=False)
