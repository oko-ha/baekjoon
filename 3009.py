# https://www.acmicpc.net/problem/3009
# 이름 : 네 번째 점
# 번호 : 3009
# 난이도 : 브론즈 III
# 분류 : 구현 기하학

import sys
x, y = [], []
for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    if a in x: x.remove(a)
    else: x.append(a)
    if b in y: y.remove(b)
    else: y.append(b)
print(*x, *y)