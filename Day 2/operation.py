# # 비교 연산자
# # 비교연산자의 결과는 Bool type이다.
#
# # 크다,작다 >,<
# print(5>1)
# # 이상,이하 >=,<=
# print(3>=3)
# #같다(same) ==
# print(3==1)
# #다르다 !=
# print(3!=100)
# #
# # #논리 연산자
#
# #and [모든 조건이 True이어야만 True]
# print(3>1 and 5<10) #true
# print(3!=5 and 3==3) #False
#
# #or [하나라도 조건이 True 이면 True]
# print(1<2 or 2<3) #True
#
# #not boolean type 반대로
# a = (3 >1) and (5>1)
# print(a)
# print(not a)
#
# #할당 연산자
#
# x=5
# # x=x+3 # 3을 추가하기
# x +=3
# y=10
# # y=y-5
# y -=5
# z=10
# # z=z*10
# z *=10
#
# #일차 함수 퀴즈
# #y= x*a + b
a = int(input("당신이 원하는 a의 값"))
b = int(input("당신이 원하는 b의 값"))
x = int(input("당신이 원하는 x의 값"))


print(f"y = {x*a+b}")










