# # a = ["apple","banana","cherry"]
# # b = []
# # for i in a:
# #     b.append((i[0]))
# # print(a)
# #
# # word_list = ["apple","banana","cherry",date"]
# # word = []
# # for list in word_list:
# #     for spell in word:
# #          if spell = 'a':
# #              word.append(list)
# # print(word)
#
# a = ["apple","banana","cherry","date"]
# b = []
# for i in a:
#     newWord = ""
#     for spell in i:
#         if not spell in 'aeoui':
#             newWord += spell
#             b.append(newWord)
# print(b)

food_List = []
travel_List = []
shopping_List = []

while True:
    a = int(input("리스트를 선택해주세요 (1.음식리스트,2.갈 곳 리스트,3.쇼핑 리스트,4.리스트 모두보기,5,종료"))
    if a == 1:
        food = input("음식리스트:")
        food_List.append(food)
    elif a == 2:
        travel = input("갈 곳 리스트:")
        travel_List .append(travel)
    elif a == 3:
        shopping = input("쇼핑 리스트:")
        shopping_List.append(shopping)
    elif a == 4:
        print(f"음식리스트는 {food_List}갈 곳 리스트는 {travel_List}쇼핑리스트는 {shopping_List}입니다")
    elif a == 5:
        print(f"음식리스트는 {food_List}갈 곳 리스트는 {travel_List}쇼핑리스트는 {shopping_List}입니다")
        break
    else:
        print("이거 아냐")











