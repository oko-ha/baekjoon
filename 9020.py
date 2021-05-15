# https://www.acmicpc.net/problem/9020
# 이름 : 골드바흐의 추측
# 번호 : 9020
# 난이도 : 실버 I
# 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline
num = []
for _ in range(int(input())):
    num.append(int(input()))
n = max(num)
primes = []
a = [False,False] + [True] * (n + 1)
for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False
b = [() for _ in range(n // 2 - 1)]
for i in range(len(primes)):
    for j in range(i, len(primes)):
        if (primes[i] + primes[j]) % 2 == 0:
            r = (primes[i] + primes[j]) // 2 - 2
            if r < len(b):
                b[r] = (primes[i], primes[j])
            else:
                break
for i in num:
    print(*b[i // 2 - 2])