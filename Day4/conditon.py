#1.조건문
#if문

# toeic = int(input("토익 점수 입력:"))
# # if toeic > 900:
# #     print("축하합니다. 장려금이 나옵니다.")
# # print("끝")
#
# #중첩 if문
# if toeic > 800:
#     print("축하합니다.")
#     if toeic > 900:
#         print("장려금이 나옵니다!")
#
#elif, else문
# shopping = int(input("구매한 금액:"))
#
# if 50000 > shopping > 30000:
#     print("주차권 1시간!")
# elif 70000 > shopping and shopping >= 50000:
#     print("주차권 2시간!")
# elif 100000 > shopping and shopping >= 70000:
#     print("주차권 3시간")
# elif shopping >= 100000:
#     print("주차권 종일")
# else:
#     print("주차권 없음")

# score = int(input("당신의 수학점수를 적으시오"))
# # if 80 > score >= 70:
# #     print("당신의 등급은 C입니다.")
# # elif 90 > score >= 80:
# #     print("당신의 등급은 B입니다.")
# # elif 100>= score >= 90:
# #     print("당신의 등급은 A입니다.")
# # else:
# #    print("과락입니다.")
# score1 = int(input("당신의 국어점수를 적으시오"))
# score2 = int(input("당신의 영어점수를 적으시오"))
#
# if 80 > (score+score1+score2)/3 >= 70:
#     print("당신의 종합등급은 C입니다.")
# elif 90 > (score+score1+score2)/3 >= 80:
#     print("당신의 종합등급은 B입니다.")
# elif 100 > (score+score1+score2)/3 >=90:
#     print("당신의 종합등급은 A입니다.")
# else:
#     print("과락입니다.")

number = int(input("당신이 원하는 숫자를 입력하시오"))

if number > 0:
    if number % 2 ==0:
        print("양의 짝수")
    else:
        print("양의 홀수")
elif number == 0:
    print("0")
else:
    if number % 2 == 0:
        print("음의 짝수")
    else:
        print("음의 홀수")




























