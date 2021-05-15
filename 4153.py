# https://www.acmicpc.net/problem/4153
# 이름 : 직각삼각형
# 번호 : 4153
# 난이도 : 브론즈 III
# 분류 : 수학, 기하학

import sys
while True:
    a = list(map(int, sys.stdin.readline().split()))
    if sum(a) == 0:
        break
    a.sort()
    if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
        print('right')
    else:
        print('wrong')