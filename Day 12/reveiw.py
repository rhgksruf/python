# num = 12345 #데이터타입 바꾸기? str,list
# numStr = str(num) #"12345"
# numList = list(numStr) # ['1','2','3','4','5']
# numList.reverse()
# numIntList = list(map(lambda x: int(x),numList))
# print(numIntList)

phonrNumber = "01033334444"
passwordNumber = ""
for index, item in enumerate(phonrNumber):
    if len(phonrNumber) - index > 4:
        passwordNumber += "*"
    else:
        passwordNumber += item
print(passwordNumber)
