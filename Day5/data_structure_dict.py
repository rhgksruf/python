# # # 자료 구조 (data_structure) - dict
# #
# # cpffee = {
# #     #'key':'value'
# #     1:'아메리카노',
# #     2:'라떼',
# #     3:'바닐라',
# # }
# # nation = {
# #     '한국':'일본',
# #     '일본':'도쿄'
# #     '중국':'베이징',
# #     '프랑스':,'파리',
# # }
# #
# # travel = {
# #     'city:['후쿠오카','벳부','나가사키','히로시마'],
# #     'food':['라멘','초밥','텐동'],
# #     'hotel':[
# #         {'이름':퍼스트스테이','가격':100000,'조식':False'}
# #         {'이름':'지니어스호텔'
# #
# # mbti = {
# #     'e':'외향적',
# #     'i':'내향적',
# #     's':'현실적',
# #     'n':'직관적',
# #     't':'이성적',
# #     'f':'감성적',
# #     'j':'계회적',
# #     'p':'즉흥적',
# #
# # }
# #
# # a = input("mbti가 어떻게 되시나요?")
# # a.lower()
# # print(f"{mbti[a[0]]} {mbti[a[1]]} {mbti[a[2]]} {mbti[a[3]]}")
# #
# movie = {
#     1:{
#         'name':'액션 영화',
#         'price': 10000,
#     },
#     2:{
#         'name':'로맨틱 코미디 영화',
#         'price':8000,
#     },
#     3:{
#         'name':'공포 영화',
#         'price':9000,
#     },
# }
# num = int(input("보고싶은 영화를 고르시오(1.액션,2.로맨틱 코미디,3.공포)"))
# age = int(input("당신의 나이를 입력해주세요"))
#
# if age<13:
#     print(f"고르신 영화는 {movie[num]['name']} 가격은 {movie[num]['price']*0.5}")
# elif age >= 60:
#     print(f"고르신 영화는 {movie[num]['name']} 가격은 {movie[num]['price'] * 0.7}")
# else:
#     print(f"고르신 영화는 {movie[num]['name']} 가격은 {movie[num]['price']}")
#
# bus = {
#     1: {'type': '시내버스',
#         'price': 1200,
#         },
#     2: {'type': '광역버스',
#         'price': 2000,
#         },
#     3: {'type': '마을버스',
#         'price': 1000,
# #         },
# }
#
# bus_number = int(input("당신이 타고 싶은 버스를 입력하시오(1.시내버스,2.광역버스,3.마을버스"))
# age1 = int(input("당신의 나이를 입력하시오"))
#
# if age1 <= 7:
#     print(f"당신이 타고싶은 버스는 {bus[bus_number]['type']} 가격은 {bus[bus_number]['price'] * 0}무료입니다")
# elif 19 >= age1 and age1 >= 8:
#     print(f"당신이 타고싶은 버스는 {bus[bus_number]['type']} 가격은 {bus[bus_number]['price'] * 0.7}")
# elif 65 <= age1:
#     print(f"당신이 타고싶은 버스는 {bus[bus_number]['type']} 가격은 {bus[bus_number]['price'] * 0}무료입니다")
# else:
#     print(f"당신이 타고싶은 버스는 {bus[bus_number]['type']} 가격은 {bus[bus_number]['price']}")































