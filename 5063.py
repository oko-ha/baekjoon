# https://www.acmicpc.net/problem/5063
# 이름 : TGN
# 번호 : 5063
# 난이도 : 브론즈 III
# 분류 : 수학, 사칙연산

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    r, e, c = map(int, input().split())
    if r < e - c:
        print("advertise")
    elif r > e - c:
        print("do not advertise")
    else:
        print("does not matter")