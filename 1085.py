# https://www.acmicpc.net/problem/1085
# 이름 : 직사각형에서 탈출
# 번호 : 1085
# 난이도 : 브론즈 III
# 분류 : 수학, 기하학

import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(min(x, y, w - x, h - y))