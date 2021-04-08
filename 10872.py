# 팩토리얼
def factorial(a):
    answer = 1
    if a > 0:
        answer = a * factorial(a - 1)
    return answer

a = int(input())
print(factorial(a))