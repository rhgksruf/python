#built-in-function
# print,input,...
#map(function,[List,str,dict,set,tutple]) : 치환하기,바꾸기
# num_list = [1,2,3,4,5]
# a = map(lambda x: x**2,num_list)
# print(list(a))
# num_List = [1,2,3,4,5,6]
# a = map(lambda x: '🥕' if x % 2 == 0  else '🐇',num_List)
# print(list(a))

fruits = ['apple','strawberry','banana','oragne']
upperList = map(lambda x: x.upper(),fruits)
lenList = map(lambda x: len(x),fruits)
print(list(upperList))
print(list(lenList))


















