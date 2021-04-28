# https://www.acmicpc.net/problem/1149
# 이름 : RGB거리
# 번호 : 1149
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
m = list(map(int, sys.stdin.readline().split()))
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]
for house in houses:
    a = house[0] + min(m[1], m[2])
    b = house[1] + min(m[0], m[2])
    c = house[2] + min(m[0], m[1])
    m = [a, b, c]
print(min(m))