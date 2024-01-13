# 일반 함수: def abc(x,y): return
# 람다(익명) 함수: lambda x,y: 한줄
# - 간단한 연산 일 때 사용
# - def abc(x,y): return ~~~
# - f(g(x)) 매개변수가 함수일때 lambda

# a = lambda x,y: x+y
# b = lambda x,y: x-y
# c = lambda x,y: x*y
# lambda x: '홀' if x % 2 == 0 else '짝'
a = lambda x: '🥕' if x % 5 == 0 else '🐰'
print(a(10))