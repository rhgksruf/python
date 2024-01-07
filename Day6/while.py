import random

#while
# a = 1
# while a < 10:
#     print(a)
#     a += 0.00000000000001

#2.
# while True:
#     num = int(input("숫자를 입력(0은 종료):"))
#     if num == 0:
#         break

# A = random.randint(1,101)
# try_num = 0
#
# while True:
#     num = int(input("숫자를 적으시오"))
#     if num > A:
#         print("down")
#         try_num += 1
#     elif num < A:
#         print("Up")
#         try_num += 1
#     else:
#         print(f"정답입니다! 때려맞춘 횟수: {try_num} ")
#         break

# num1 = 0
# while True:
#      num = int(input("숫자[0종료]:"))
#      if num != 0:
#         num1 += num
#      else:
#          print(f"총합은 {num1}")
#          break

# print("일본여행 todoList")
# foodList = []
# goList = []
#
# while True:
#     List = int(input("작성하고 싶은 리스트 선택하시오[1.먹고 싶은것,2.가고 싶은것3.그만 작성하기]"))
#     if List == 1:
#         eat = input("먹고 싶은것을 적으시오")
#         foodList.append(eat)
#
#     elif List == 2:
#         go = input("가고 싶은 곳을 적으시오")
#         goList.append(go)
#     elif List == 3:
#         print(f"{foodList}")
#         print(f"{goList}")
#     else:
#         print("종료")
#         break


while True:
    num0 = int(input("1.더하기,2.빼기,3.곱하기,4.종료"))
    if num0 == 1:
        num1 = int(input("원하는 수"))
        num2 = int(input("원하는 수"))
        print(f"더한 값은 {num1+num2}입니다.")
    elif num0 == 2:
        num1 = int(input("원하는 수"))
        num2 = int(input("원하는 수"))
        print(f"뺀 값은 {num1-num2}입니다.")
    elif num0 == 3:
        num1 = int(input("원하는 수"))
        num2 = int(input("원하는 수"))
        print(f"곱한 값은 {num1*num2}입니다.")
    elif num0 == 4:
        print("종료")
        break



