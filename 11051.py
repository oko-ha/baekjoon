# https://www.acmicpc.net/problem/11051
# 이름 : 이항 계수 2
# 번호 : 11051
# 난이도 : 실버 I
# 분류 : 수학, 다이나믹 프로그래밍

import sys
from math import factorial
n, k = map(int, sys.stdin.readline().split())
print((factorial(n) // (factorial(k) * factorial(n-k))) % 10007)