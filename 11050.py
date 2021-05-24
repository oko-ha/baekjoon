# https://www.acmicpc.net/problem/11050
# 이름 : 이항 계수 1
# 번호 : 11050
# 난이도 : 브론즈 I
# 분류 : 수학, 구현, 조합론

import sys
from math import factorial
n, k = map(int, sys.stdin.readline().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))