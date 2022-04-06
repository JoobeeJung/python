#12Fact.py : Factorial
# 4! = 4 * 3 * 2 * 1
#   = 1 * .... * 4

def factorial(n):
    y = 1
    for x in range(1, n+1):
        y = y * x
    return y

def fact(n):
    """
    multi line comment
    함수 등의 내용을 기술해 준다.
    파라미터 : 양의 정수
    리턴 : 팩토리얼 값
    """
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


input = int(input("Insert Number : "))
result = factorial(input)
print("result = " , result)
"""
print("-" * 80)
result = fact(input)
print("recursive = ", result)
"""
print(fact.__doc__)