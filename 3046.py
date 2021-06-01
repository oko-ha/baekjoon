# https://www.acmicpc.net/problem/3046
# 이름 : R2
# 번호 : 3046
# 난이도 : 브론즈 V
# 분류 : 수학, 구현, 사칙연산

import sys
r1, s = map(int, sys.stdin.readline().split())
print(s * 2 - r1)