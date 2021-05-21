# https://www.acmicpc.net/problem/2981
# 이름 : 검문
# 번호 : 2981
# 난이도 : 골드 V
# 분류 : 수학, 정수론, 유클리드 호제법

import sys
import math
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    if i > 0:
        if i == 1:
            g = abs(n - temp)
        else:
            g = math.gcd(abs(n - temp), g)
    temp = n
num = [g]
for i in range(2, math.ceil(g**0.5) + 1):
    if g % i == 0:
        num.append(i)
        num.append(g // i)
num = list(set(num))
num.sort()
print(*num)