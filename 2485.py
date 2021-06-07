# https://www.acmicpc.net/problem/2485
# 이름 : 가로수
# 번호 : 2485
# 난이도 : 실버 IV
# 분류 : 수학, 정수론, 유클리드 호제법

import sys
from math import gcd
input = sys.stdin.readline
n = int(input())
for i in range(n):
    number = int(input())
    if i > 1:
        t = number - temp
        g = gcd(g, t)
    elif i > 0:
        g = number - temp
    else:
        first = number
    temp = number
print((number - first) // g - n + 1)