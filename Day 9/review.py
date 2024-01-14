
# List = [i for i in range(1,21) if i % 2 != 1]
# print(List)
#
# b = [i for i in range(11) if i > 5]
# print(b)
#
# word = ['apple','banana','cherry','date']
# c = [i[0] for i in word]
# print(c)
#
# a = [i ** 2 for i in range(1,6)]
# print(a)

my_string = 'apple'
word_LIst = [i for i in my_string]
word_LIst.reverse()
newword = ''
for i in word_LIst:
    newword += i
print(newword)

todoList = ['programming','sleeping','game','eating']
finished = [True,True,False,False]
havetoList = []
for index,item in enumerate(finished):
    if not item:
        havetoList.append(todoList[index])
print(havetoList)





























































































































