# movie = {
#     1: {'name' : '액션영화',
#     'price' : 10000},
#     2:{'name' : '로맨틱 코미디',
#        'price' : 8000},
#     3 : {'name' : '공포영화',
#        'price' : 9000},
# }
#
# for i in range(1,len(movie.keys())+1):
#     print(f"{movie[i]['name'],movie[i]['price']}")
# a = int(input("당신이 원하는 영화의 종류를 고르시오(1.액션영화,2.로맨틱 코미디,3.공포영화"))
# age = int(input("당신의 나이:"))
#
# if age < 13:
#     print(f"당신이 고르신 영화는 {movie[a]['name']}이고 가격은 {movie[a]['price']*1/2}입니다")
# elif age >= 60:
#     print(f"당신이 고르신 영화는 {movie[a]['name']}이고 가격은 {movie[a]['price']*7/10}입니다")
# else:
#     print(f"당신이 고르신 영화는 {movie[a]['name']}이고 가격은 {movie[a]['price']}입니다)")

# LOL_List = []
# win_List = []
# print("리그오브 레전트 챔피언 및 승률 리스트")
# while True:
#     a = int(input("1.선택한 챔 고르기,2.챔피언의 승률 쓰기3.목록 보기4.종료"))
#     if a == 1:
#         champion = input("당신이 선택한 챔을 고르시오")
#         LOL_List.append(champion)
#     elif a == 2:
#         win_grath = float(input("당신이 선택한 챔의 승률을 쓰시오"))
#         win_List.append(win_grath)
#     elif a == 3:
#         print(f"챔피언 {LOL_List}이고 승률은 {win_List}%입니다")
#     elif a == 4:
#         print(f"챔피언 {LOL_List}이고 승률은 {win_List}%입니다")
#         break
#     else:
#         print("다시")

data = []

champion_List = []
games_List = []
items_List = []
line_List = []

while True:
    choice = int(input('1.게임 기록하기,2.종료하기'))
    if choice == 1:
        champion = input("당신이 한 챔을 적으시오")
        games = input("게임 결과(승/패)")
        items = input("당신이 쓴 아이템들을 모두 적으시오")
        line = input("당신이 선 라인을 적으시오")

        listItem = items.split()
        temp = {
            'champion': champion,
            'games': games,
            'items': listItem,
            'line': line,
        }
        data.append(temp)
    elif choice == 2:
        print(data)





