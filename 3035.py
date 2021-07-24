# https://www.acmicpc.net/problem/3035
# 이름 : 스캐너
# 번호 : 3035
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline
R, C, ZR, ZC = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
for ar in arr:
    for _ in range(ZR):
        for a in ar:
            print(a * ZC, end='')
        print()