# https://www.acmicpc.net/problem/12865
# 이름 : 평범한 배낭
# 번호 : 12865
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 배낭 문제

import sys
n, k = map(int, sys.stdin.readline().split())
item = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
value = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if item[i-1][0] <= j:
            value[i][j] = max(item[i-1][1] + value[i-1][j-item[i-1][0]], value[i-1][j])
        else:
            value[i][j] = value[i-1][j]
print(value[n][k])