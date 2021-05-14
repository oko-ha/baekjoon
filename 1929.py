# https://www.acmicpc.net/problem/1929
# 이름 : 소수 구하기
# 번호 : 1929
# 난이도 : 실버 II
# 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [False,False] + [True]*(m-1)
primes = {}
for i in range(2, m + 1):
  if a[i]:
    primes[i] = 1
    for j in range(2*i, m+1, i):
        a[j] = False
for i in range(n, m + 1):
    if i in primes:
        print(i)