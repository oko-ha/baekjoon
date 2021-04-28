# https://www.acmicpc.net/problem/2579
# 이름 : 계단 오르기
# 번호 : 2579
# 난이도 : 실버 III
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
first = int(sys.stdin.readline().rstrip())
stairs = [int(sys.stdin.readline().strip()) for _ in range(n-1)]
m = [0, 0, first, first]
for stair in stairs:
    a, b, c, d = m[0], m[1], m[2], m[3]
    m = [c, d, d + stair, max(a, b) + stair]
print(max(m[2], m[3]))