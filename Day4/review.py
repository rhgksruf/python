# import random
#
# A = input("문자 한 개를 입력해주세요")
# if A.isalpha():
#     print("맞음")
# else:
#     print("아님")
#
#
# num = int(input("숫자를 하나 말씀해 주세요"))
# if num & 2 ==0:
#     print("홀수입니다")
# else:
#     print("짝수입니다")
#
# num2 = random.randint(1,20)
# choice = int(input("1~100까지 숫자를 적으시오"))
# if choice > num2:
#     print("Down")
# elif choice < num2 :
#     print("Up")
# else:
#     print("정답입니다")
# choice = int(input("1~100까지 숫자를 적으시오"))
# if choice > num2:
#     print("Down")
# elif choice < num2 :
#     print("Up")
# else:
#     print("정답입니다")
# choice = int(input("1~100까지 숫자를 적으시오"))
# if choice > num2:
#     print("Down")
# elif choice < num2 :
#     print("Up")
# else:
#     print("정답입니다")
# choice = int(input("1~100까지 숫자를 적으시오"))
# if choice > num2:
#     print("Down")
# elif choice < num2 :
#     print("Up")
# else:
#     print("정답입니다")
# choice = int(input("1~100까지 숫자를 적으시오"))
# if choice > num2:
#     print("Down")
# elif choice < num2 :
#     print("Up")
# else:
#     print("정답입니다")
#
# kor = int(input("국어점수:"))
# math = int(input("수학점수"))
# eng = int(input("영어점수"))
# avg = (kor + eng + math)/3
# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("C")
# else:
#     print("과락")


choice1 = int(input("원하는 음료의 숫자를 말하시오(1~3)"))
money = int(input("원하시는 금액을 말하시오"))
if choice1 == 1:
    if 3000 > money:
        print("금액이 부족합니다.")
    else:
        print(f"당신은 아메리카노를 선택하셨습니다.거스름돈은{money-3000}입니다.")
elif choice1 == 2:
    if 4000 > money:
        print("금액부족")
    else:
        print(f"당신은 레몬에이드를 선택하셨습니다.거스름돈은{money - 4000}")

elif choice1 == 3:
    if 3500 > money:
        print("금액부족")
    else:
        print(f"당신은 카페라떼를 선택하셨습니다.거스름돈은{money - 3500}")

