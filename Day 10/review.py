import random
#
# numList = [random.randint(1,101) for i in range(10)]
#
# evenList = []
# oddList = []
#
# for i in numList:
#     if i % 2 == 0:
#         evenList.append(i)
#     else:
#         oddList.append(i)
#
# print(numList)
# print(evenList)
# print(oddList)
#
# numberList = [random.randint(1,31) for i in range(10)]
# zooList = []
# for i in numberList:
#     if 1 <= i and i <= 10:
#         zooList.append('🐰')
#     elif 11 <= i and i <= 20:
#         zooList.append('🙉')
#     else:
#         zooList.append('🐶')
# print(numberList)
# print(zooList)

def makeList(m,n):
    return [random.randint(m,n+1) for i in range(5)]

lambda m,n: [random.randint(m,n+1) for i in range(5)]





