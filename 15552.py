# https://www.acmicpc.net/problem/15552
# 이름 : 빠른 A+B
# 번호 : 15552
# 난이도 : 브론즈 II
# 분류 : 수학, 구현, 사칙연산

import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    print(sum(map(int, sys.stdin.readline().split())))