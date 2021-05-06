# https://www.acmicpc.net/problem/1978
# 이름 : 소수 찾기
# 번호 : 1978
# 난이도 : 실버 IV
# 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline

input()
numbers = list(map(int, input().split()))

n=max(numbers)
a = [False,False] + [True]*(n-1)
primes = {}

for i in range(2,n+1):
  if a[i]:
    primes[i] = 1
    for j in range(2*i, n+1, i):
        a[j] = False

cnt = 0
for number in numbers:
    if number in primes:
        cnt += 1
print(cnt)