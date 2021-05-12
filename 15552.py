# https://www.acmicpc.net/problem/15552
# 이름 : 빠른 A+B
# 번호 : 15552
# 난이도 : 브론즈 II
# 분류 : 수학, 구현, 사칙연산

import sys
input = sys.stdin.readline
for i in range(int(input())):
    print(sum(map(int, input().split())))