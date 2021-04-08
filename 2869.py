# https://www.acmicpc.net/problem/2869
# 이름 : 달팽이는 올라가고 싶다
# 번호 : 2869
# 난이도 : 브론즈 I
# 분류 : 수학

import sys
import math
a, b, c = map(int, sys.stdin.readline().split())

i = math.ceil((c - a) / (a - b))
print(i + 1)