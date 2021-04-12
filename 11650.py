# https://www.acmicpc.net/problem/11650
# 이름 : 좌표 정렬하기
# 번호 : 11650
# 난이도 : 실버 V
# 분류 : 정렬

import sys
dot = []
for _ in range(int(sys.stdin.readline().rstrip())):
    dot.append(list(map(int, sys.stdin.readline().split())))
dot = sorted(dot, key=lambda x : [x[0], x[1]])
for x, y in dot:
    print(x, y)