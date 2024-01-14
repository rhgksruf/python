# #map(): 치환,변경
# x = [1,2,3,4,5]
# newList = list(map(lambda x: x +20,x))
# print(newList)
#
# # filter(): 거름:
# newList1 = list(filter(lambda x: x>3,x))
# print(newList1)
#
# evenList = list(filter(lambda x: x%2 == 0, x))
# print(evenList)

# List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List1 = list(filter(lambda x: x % 3 != 0, List))
#
# List2 = list(filter(lambda x: x ** 2>25,List))
# print(List2)

fruits = ['shineMusket', 'mandarin', 'peach', 'apple', 'strawberyy', 'banana', 'orange']
# fruits_List = list(filter(lambda x: len(x) >= 6, fruits))
# print(fruits_List)
#
# fruits_List1 = list(filter(lambda x: 's' in x,fruits))
# fruits_List1 = list(filter(lambda x: x.count('s')>0,fruits))
# print(fruits_List1)

fruits_num = list(filter(lambda x:len(x)%2==0 and x.count('a')>=2,fruits))
print(fruits_num)




















