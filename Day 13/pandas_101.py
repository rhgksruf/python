import pandas
import random
from faker import Faker

fake = Faker('ko_KR')
# sereis, dataframe

data = {
    'name': [fake.name() for i in range(500)],
    'ages': [random.randint(20,61) for x in range(500)]
}

a = pandas.DataFrame(data)
a.to_csv('megacoffee.csv', encoding='utf-8-sig', index=False)











