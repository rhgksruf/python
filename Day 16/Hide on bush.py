import requests
from bs4 import BeautifulSoup


# url = ('https://www.op.gg/summoners/kr/%EC%96%B4%EB%A6%AC%EA%B3%A0%EC%8B%B6%EB%8B%A4-KR1')
# response = requests.get(url)
# data = response.text
# soup = BeautifulSoup(data, 'html.parser')
# clothesList = soup.find(id='champion-box').find_all('li')



class Doran:
    def __init__(self):
        self.name = 'Doran'
        self.champion = ['나르', '아트록스', '레넥톤']
        self.result = [79, 60]
        self.kda = [2.7, 3.4, 2.6]
        self.win = [66.7, 69, 46.2]


class Peanut:
    def __init__(self):
        self.name = 'Peanut'
        self.champion = ['리신', '세주아니', '니달리']
        self.result = [124, 77]
        self.kda = [5.31, 3.63, 3.71]
        self.win = [57, 65.6, 64.7]


class Zeka:
    def __init__(self):
        self.name = 'Zeka'
        self.champion = ['아지르', '아리', '아칼리']
        self.result = [60, 43]
        self.kda = [3.6, 5.2, 5]
        self.win = [56.3, 50, 70.4]


class Viper:
    def __init__(self):
        self.name = 'viper'
        self.champion = ['카이사', '이즈리얼', '루시안']
        self.result = [80, 61]
        self.kda = [6.1, 6.3, 7.2]
        self.win = [53.8, 57.1, 71.4]


class Delight:
    def __init__(self):
        self.name = 'Delight'
        self.champion = ['라칸', '레오나', '알리스타']
        self.result = [76, 58]
        self.kda = [5, 2.4, 3.9]
        self.win = [62, 50, 52]


class DnDn:
    def __init__(self):
        self.name = 'DnDn'
        self.champion = ['크샨테', '레넥톤', '잭스']
        self.result = [16, 39]
        self.kda = [2.4, 2.1, 0.6]
        self.win = [35.7, 37.5, 0]


class Sylvie:
    def __init__(self):
        self.name = 'Sylvie'
        self.champion = ['오공', '바이', '비에고']
        self.result = [12, 39]
        self.kda = [1.6, 2, 2.6]
        self.win = [68.4, 72.6, 70.2]


class Callme:
    def __init__(self):
        self.name = 'Callme'
        self.champion = ['아지르', '탈리아', '오리아나']
        self.result = [4, 6]
        self.kda = [1.1, 5.2, 1.8]
        self.win = [25, 66.7, 33.3]


class Jiwoo:
    def __init__(self):
        self.name = 'Jiwoo'
        self.champion = ['자야', '아펠리우스', '바루스']
        self.result = [10, 17]
        self.kda = [3.5, 1.4, 3.9]
        self.win = [42.9, 22.2, 50]


class Peter:
    def __init__(self):
        self.name = 'Peter'
        self.champion = ['라칸', '유미', '노틸러스']
        self.result = [17, 31]
        self.kda = [3.7, 6.2, 2.1]
        self.win = [38.9, 37.5, 28.6]

print(Doran())

