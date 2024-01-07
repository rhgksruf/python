# #컴프리헨션
# compre = [i for i in range(101)]
# compre1 = [i**2 for i in range(101)]
# print(compre)
# print(compre1)

# #유저에게 영단어를 입력받고 > 대문자화된 각각의 스펠링이 담긴 리스트 출력
# a = input("영단어:")
# # word = [i for i in a.upper()]
# # print(word)
#
# #컴프리헨션 조건
#
# # List = [i for i in range(1001) if i % 2 != 0]
# # print(List)
#
# word1 = [i for i in a if i not in 'aeiou']
# print(word1)

print(['👋' if str(i%10) in '369' or str(int(i/10)) in '369' else i for i in range(101)])












