num = "onetwothreefourfivesixseveneightnine"
numList = ['zero','one','two','three','four','five','six','seven','eight','nine']
for index, item in enumerate(numList):
    if item in num:
        num = num.replace(item, str(index))
print(num)
