# https://www.acmicpc.net/problem/1010
# 이름 : 다리 놓기
# 번호 : 1010
# 난이도 : 실버 V
# 분류 : 수학, 다이나믹 프로그래밍, 조합론

import sys
from math import factorial
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    print((factorial(m) // (factorial(n) * factorial(m-n))))