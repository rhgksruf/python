    #print()출력
    #input()대답
    #int()정수화
    #str() 문자화
    #ytpe()무슨 타입인지 알려줌
    # print(type(1.23))

    # print("5/2") # 실수 표현
    # print("5//2") # 정수(몫)
    # print("5%2") # 나머지


year = int(input("당신이 태어난 연도는?"))
print(f"당신의 만나이는 {2023-year}이군요")

A = float(input("첫 번째 숫자를 입력하세요"))
B = float(input("두 번째 숫자를 입력하세요"))
C = float(input("세 번째 숫자를 입력하세요"))

print(f"평균은 {(A+B+C)/3}이군요.")

won = float(input("당신이 환전하고 싶은 금액은 얼마 입니까?"))

print(f"엔의 환율은{won*0.11}엔 이고 달러는{won*0.00077}달러 입니다")

K = float(input("당신이 원하는 Km거리를 입력하시오"))
print(f"이것을 마일로 변환 했을 때 거리는 {K*0.621371}mile입니다.")

C = float(input("당신이 원하는 섭씨 온도를 말하시오"))
print(f"화시온도는 {C*59+32}입니다.")

M = float(input("당신의 키(M)를 말하시오"))
kg = float(input("당신의 몸무게(kg)를 말하시오"))

print(f"당신의 bmi지수는 {kg/(M**2)}입니다.")




