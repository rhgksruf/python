import random
import pandas
from faker import Faker
fake = Faker('ko_KR')

movie0 = ['웡카', '시민 덕희', '외계인', '너의 이름은', '위시', '도그맨']
moviePer = [35, 25, 10, 10, 10, 10]
popcorn0 = ['일반', '카라멜', '치즈', '어니언', '구매 안함']
popcornPer = [20, 10, 10, 10, 50]
snack = ['맛밤', '오징어', '나초', '핫도그', '구매 안함']
snackPer = [5, 5, 20, 10, 60]
drink0 = ['콜라', '사이다', '환타', '제로 콜라', '에이드', '물', '아메리카노', '구매 안함']
drinkPer = [15, 10, 10, 15, 10, 20, 10, 10]
age0 = [20, 30, 40, 50, 60]
agePer = [40, 30, 15, 10, 5]
times = ['조조', '일반', '심야']
timePer = [20, 70, 10]
payments = ['현금', '체크 카드', '신용 카드', '카카오 페이', '삼성 페이']
paymentsPer = [5, 10, 30, 5, 50]



Data = {
    'movie': [random.choices(movie0, weights=moviePer, k=1)[0] for i in range(10000)],
    'popcorn': [random.choices(popcorn0, weights=popcornPer, k=1)[0] for x in range(10000)],
    'name': [fake.name() for c in range(10000)],
    'age': [random.choices(age0, weights=agePer, k=1)[0] for p in range(10000)],
    'drink': [random.choices(drink0, weights=drinkPer, k=1)[0] for b in range(10000)],
    'times': [random.choices(times, weights=timePer, k=1)[0] for u in range(10000)],
    'snacks': [random.choices(snack, weights=snackPer, k=1)[0] for o in range(10000)],
    'payments': [random.choices(payments, weights=paymentsPer, k=1)[0] for y in range(10000)]
}

a = pandas.DataFrame(Data)
a.to_csv('cgv.csv', encoding='utf-8-sig', index=False)