# https://www.acmicpc.net/problem/1247
# 이름 : 부호
# 번호 : 1247
# 난이도 : 브론즈 III
# 분류 : 수학, 사칙연산, 임의 정밀도/큰 수 연산

import sys
input = sys.stdin.readline
for _ in range(3):
    s = 0
    for _ in range(int(input())):
        s += int(input())
    if s > 0:
        print("+")
    elif s < 0:
        print("-")
    else:
        print("0")