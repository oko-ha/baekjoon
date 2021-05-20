# https://www.acmicpc.net/problem/5086
# 이름 : 배수와 약수
# 번호 : 5086
# 난이도 : 브론즈 III
# 분류 : 수학, 구현

import sys
while True:
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        break
    if y % x == 0:
        print('factor')
    elif x % y == 0:
        print('multiple')
    else:
        print('neither')