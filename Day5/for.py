# # #제어문(control statement)
# # #프로그램이 순차적 진행
# # #1) 조건문 [해당 코드를 실행 할지 말지]
# # #2) 반복문 [해당 코드를 n번 반복]
# #
# # for x in range(101):
# #     if x % 15 == 0:
# #         print(x)
#
# for i in 'snow':
#     print(i)
#
# for i in ['apple','banana','kiwi']:
#     print(i)

#영단어를 입력했을 때, BbbbB
# -> 대문자를 소문자로 소문자는 대문자로 bBBBb
#2.영단어를 입력했을 때, 모음이 빠진 영단어로 보여주기
#apple ->ppl

word = input("원하는 영단어를 쓰시오")
text = ''
for i in word:
    if i.isupper():
        text += i.lower()
    else:
        text += i.upper()
print(text)




