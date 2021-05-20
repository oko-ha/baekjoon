# https://www.acmicpc.net/problem/1002
# 이름 : 터렛
# 번호 : 1002
# 난이도 : 실버 IV
# 분류 : 수학, 기하학

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        n = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
        if abs(r1 - r2) < n < r1 + r2:
            print(2)
        elif abs(r1 - r2) == n or r1 + r2 == n:
            print(1)
        else:
            print(0)