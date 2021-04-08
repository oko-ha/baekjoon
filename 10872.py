# https://www.acmicpc.net/problem/10872
# 이름 : 팩토리얼
# 번호 : 10872
# 난이도 : 브론즈 III
# 분류 : 수학, 구현

def factorial(a):
    answer = 1
    if a > 0:
        answer = a * factorial(a - 1)
    return answer

a = int(input())
print(factorial(a))