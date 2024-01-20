# iphoneList = ['iphone13', 'iphone13max', 'iphone14', 'iphone14plus', 'iphone15']
# iphonePriceList = [1000000, 1200000, 1300000, 1350000, 1500000]

# zip[지퍼]
# print(list(zip(iphoneList,iphonePriceList)))

# print([{'아이폰':phone,'가격':price}for phone,price in zip(iphoneList,iphonePriceList)])

# alpha = ['a','b','c','d','e']
# numbers = [1,2,3,4,5]
# print([{'알파벳':alphabat,'숫자':number} for alphabat,number in zip(alpha,numbers)])


text = "apple banana apple strawberry banana"
wordList = text.split()
wordLenList = list(map(lambda x:len(x), wordList))

print([{'단어': word,'글자 수':length} for word,length in zip(wordList,wordLenList)])






























