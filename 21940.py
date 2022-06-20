# https://www.acmicpc.net/problem/21940
# 이름 : 가운데에서 만나기
# 번호 : 21940
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 플로이드-워셜

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
dp = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    dp[A][B] = T
K = int(input())
C = list(map(int, input().split()))

def floyd():
    for k in range(1, N + 1):
        dp[k][k] = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

def answer():
    ans = INF
    dist = [0] * (N + 1)
    for i in range(1, N + 1):
        temp = 0
        for c in C:
            if temp < dp[c][i] + dp[i][c]:
                temp = dp[c][i] + dp[i][c]
        dist[i] = temp
        if ans > temp:
            ans = temp
    for i in range(1, N + 1):
        if ans == dist[i]:
            print(i, end = ' ')

floyd()
answer()