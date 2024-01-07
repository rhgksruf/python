import random
# 제어문
# 조건문
# - if[코드 실행 조건 유뮤]
# 반복문
# for문 [코드를 n번 실행]

#for문 - range()
# for x in range(20):
#     print(f"{x}. ddddddddddd")

# a = int(input("원하는 정수")) + 1
# sum = 0
# for x in range(a):
#     sum = sum + x # 0, 1, 3(1+2), ...
# print(sum)

# num = int(input("원하는 정수"))
# sum = 0
# for i in range(num):
#         sum += i
# sum = (num * (num-1))/2
# print(sum)
#
# for x in range(100):
#     if not(x % 3 != 0 or x % 5 != 0):
#         print(x)

#for x in 문자열,리스트

# text = ''
# for x in 'megacoffee':
#     if x.isupper():
#         text += x.lower()
#     else:
#         text += x.upper()
# print(text)

#모음제거 프로그램
# A = input('문자 입력')
# text = ''
# for x in A:
#     # if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x:
#     #     pass
#     else:
#         text += x

# nation = ['미국','일본','중국','영국','프랑스']
#
# for x in nation:
#     print(x)
#
# num = []
# for i in range(100):
#     num.append(random.randint(0,10001))

# 1번
# sum = 0
# for i in num:
#     sum += i
# print(sum/100)

# 2번
# print(sum(num)/len(num))

#3번 - 정수 랜덤[] 10개 채워주고 -> 리스트의 값의 제곱을 한 리스트
#랜덤 리스트 - [2,1,5,1,6,7]

# text = []
# for i in range(10):
#     text.append(random.randint(1,101))
#
# double_num = []
# for i in text:
#     double_num.append(i**2)
#
# print(text)
# print(double_num)


for index,item in enumerate("asdflksfj"):
    print(index,item)










