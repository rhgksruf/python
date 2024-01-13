#substract 함수: a-b 돌려주기
#multiply 함수: a*b 돌려주기
#sniffling 함수 : 홀수 or 짝수인지 돌려주기
#makeList 함수: n정수를 주었을 때, 0~n의 리스트를 돌려주기

def substract(a,b):
    return a-b
print(f"{substract(4,2)}")

def multiply(a,b):
    return a*b
print(f"{multiply(5,3)}")

def sniffling(a):
    if a%2==0:
        return "짝수"
    else:
        return "홀수"
print(f"{sniffling(3)}")

def makeList(n):
    return [i for i in range(n+1)]
print(f"{makeList(20)}")
