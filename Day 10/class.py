# # int, float, bool, dict, list, tuple, set
#
# # 객체지향 프로그래밍[Object Oriented Programming]
#
# #  나만의 데이터 타입 만들자
# # 기본형 -> 구조체 ->[struct](기본형 모음) -> 클래스[class](구조체[변수들] + 함수들)
# # height[float] -> student[str,int,int]
#
#
# # class Dog:
# #     def __init__(self):
# #         self.breed = '말티즈'
# #         self.snackList = ['개껌','개사료']
# #
# #     def bark(self):
# #         print('멍멍!')
# # a = Dog()
# # a.bark()
# # b = Dog()
# # b.bark()
#
# class Burger:
#     def __init__(self, x, y):
#         self.bread = x
#         self.ingredients = y
#         self.source = '마요네즈'
#
#     def addIngredient(self, x):
#         self.ingredients.append(x)
#
# # 인스턴스
#
# c = Burger('플랫 브래드', ['새우','에그마요','아보카도'])
# d = Burger('화이트', ['베이컨','양상추','피클'])
#
#
# #너가 어떠한 프로그래밍을 만들지 결정을 해야 클래스를 정의를 할 수 있음
# # 강아지 키우기
# class Dog:
#     def __init__(self, x):
#         self.name = x
#         self.hp = 100  #최대체력 200까지
#         self.state = 'happy'
#         self.hungry = 0
#         self.friends = []
#
#     def eating(self):
#         if self.hp < 200:
#             self.hp += 10
#         else:
#             print("체력이 꽉 찼습니다")
#
#
# a = Dog('jenny')
# for i in range(100):
#     print(f"{i}")
#     a.eating()





# a.hp = 300 금기 [변수를 함부로 변경하면 안됌]


#강아지 펫 보험 사이트 데이터 관리
# class Dog:
#     def __init__(self,x,y,z):
#         self.age = x
#         self.surgeryList = y
#         self.gender = z

# 클래스 = 변수들[명사/상태] + 함수들[동사/동작]
