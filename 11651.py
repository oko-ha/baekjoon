# https://www.acmicpc.net/problem/11651
# 이름 : 좌표 정렬하기 2
# 번호 : 11651
# 난이도 : 실버 V
# 분류 : 정렬

import sys
dot = []
for _ in range(int(sys.stdin.readline().rstrip())):
    dot.append(list(map(int, sys.stdin.readline().split())))
dot = sorted(dot, key=lambda x : [x[1], x[0]])
for x, y in dot:
    print(x, y)