# https://www.acmicpc.net/problem/9020
# 이름 : 골드바흐의 추측
# 번호 : 9020
# 난이도 : 실버 I
# 분류 : 

import sys
input = sys.stdin.readline
primes = {}
a = [False,False]
for _ in range(int(input())):
    n = int(input())
    a += [True] * (n - len(a) + 1)
    for i in range(2, n + 1):
        if a[i]:
            primes[i] = 1
            for j in range(2 * i, n + 1, i):
                a[j] = False
    