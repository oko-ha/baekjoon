# https://www.acmicpc.net/problem/11580
# 이름 : Footprint
# 번호 : 11580
# 난이도 : 브론즈 I
# 분류 : 구현, 시뮬레이션

import sys
input = sys.stdin.readline
L = int(input())
d = {'E':(1, 0), 'W':(-1, 0), 'S':(0, -1), 'N':(0, 1)}
x, y = 0, 0
footprint = {(x, y)}
for cmd in input().strip():
    x, y = x + d[cmd][0], y + d[cmd][1]
    footprint.add((x, y))
print(len(footprint))