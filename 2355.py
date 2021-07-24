# https://www.acmicpc.net/problem/2355
# 이름 : 시그마
# 번호 : 2355
# 난이도 : 브론즈 III
# 분류 : 수학, 사칙연산

import sys
A, B = map(int, sys.stdin.readline().split())
print(int((A + B) * (abs(A - B) + 1) / 2))