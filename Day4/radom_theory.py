import random

#random.randint("시작","끝")#정수만
# random.choice(리스트)
# random.uniform("시작","끝") 실수 아무거나 하나 뽑기
# random.shuffle(리스트) 리스트가 랜덤으로 섞임

# #len() #문자열, 리스트의 길이를 도출 하는 함수
# # len([1,2,3,4,5]) # 5
# lang = input("입력")
# len("mega") #4
#
# do = input("할일 적어")
# todolist = do.split()
# random.shuffle(todolist)
# print(f"크리스마스 할일: {todolist}")

lotto = []
# a = random.randint(1,45)
# b = random.randint(1,45)
# c = random.randint(1,45)
# d = random.randint(1,45)
# e = random.randint(1,45)
# f = random.randint(1,45)
lotto.append(random.randint(1,45))
lotto.append(random.randint(1,45))
lotto.append(random.randint(1,45))
lotto.append(random.randint(1,45))
lotto.append(random.randint(1,45))
lotto.append(random.randint(1,45))
lotto.sort()
print(lotto)