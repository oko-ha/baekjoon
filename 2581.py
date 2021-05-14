# https://www.acmicpc.net/problem/2581
# 이름 : 소수
# 번호 : 2581
# 난이도 : 실버 V
# 분류 : 수학, 정수론, 소수판정

import sys
input = sys.stdin.readline
m = int(input())
n = int(input())
prime = []
for i in range(m, n + 1):
    for j in range(2, i + 1):
        if i == j:
            prime.append(i)
        elif i % j == 0:
            break
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))