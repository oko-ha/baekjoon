# https://www.acmicpc.net/problem/10870
# 이름 : 피보나치 수 5
# 번호 : 10870
# 난이도 : 브론즈 II
# 분류 : 수학, 다이나믹 프로그래밍

def fibonacci(n):
    ans = 1
    if n > 2:
        ans = fibonacci(n - 2) + fibonacci(n - 1)
    elif n > 0:
        return 1
    else:
        return 0
    return ans

n = int(input())
print(fibonacci(n))