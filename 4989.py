# https://www.acmicpc.net/problem/4989
# 이름 : 베르트랑 공준
# 번호 : 4989
# 난이도 : 실버 II
# 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline
primes = {}
a = [False,False]
while True:
    n = int(input())
    if n == 0:
        break
    m = 2 * n
    a += [True]*(m - len(a) + 1)
    for i in range(2, m + 1):
        if a[i]:
            primes[i] = 1
            for j in range(2*i, m+1, i):
                a[j] = False
    cnt = 0
    for i in range(n + 1, m + 1):
        if i in primes:
            cnt += 1
    print(cnt)