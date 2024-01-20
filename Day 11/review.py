# names = ["nami","ahri","jayce","garen","ivern","vex","jinx"]
# def solution(riders):
#     newList = []
#     for index,item in enumerate(riders): #enumerate
#         if index % 5 == 0:
#             newList.append(item)
#         return newList
#     print(newList)
#
# coffee = ['아메리카노','라뗴','연유라뗴','바닐라커피','디카페인커피','맥심커피']
#
# evencoffee = [item for index, item in enumerate(coffee) if index % 2 == 1]
# print(evencoffee)
#
#
# def solution(numList):
#     if len(numList) == 1:
#         return [-1]
#     else:
#         numList.remove(min(numList))
#         return numList
# print(solution([4,1,2,3]))

def solution(string):
    if string.isdigit():
        return True
    else:
        return False



