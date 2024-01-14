# reduce
from functools import reduce

# numList = [1, 2, 3, 4, 5]
# result = reduce(lambda acc,cur: acc+cur, numList)
# factorial = reduce(lambda acc,cur: acc*cur, numList)
# print(result)
# print(factorial)


# def megastudy(call-back 함수):{}
# f(x) = x+ 10
# => f(1) = 11
# => f(2) = 12 ...
# f(g(x)) = ~~

# effs = [] recipe = 콜백함수
def eggCooking(eggs, index, recipe):
    recipe(eggs[index])
    print('요리완료!')

eggs = ['🥚','🥚','🥚']

def makeSandwich(egg):
    egg = '🍔'
def makeburger(egg):
    egg = '🍕'
def makefrank(egg):
    egg = '🍟'

print(eggs)
eggCooking(eggs,0,makeburger)
print(eggs)

