# https://www.acmicpc.net/problem/11562
# 이름 : 백양로 브레이크
# 번호 : 11562
# 난이도 : 골드 III
# 분류 : 그래프 이론, 플로이드-워셜

import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
dp = [[INF] * n for _ in range(n)]
for _ in range(m):
    u, v, b = map(int, input().split())
    dp[u-1][v-1] = 0
    dp[v-1][u-1] = b ^ 1

def floyd():
    for k in range(n):
        dp[k][k] = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

floyd()
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])