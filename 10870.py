# 피보나치 수 5
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