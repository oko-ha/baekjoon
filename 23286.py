# https://www.acmicpc.net/problem/23286
# 이름 : 허들 넘기
# 번호 : 23286
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 데이크스트라, 플로이드-워셜

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, T = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
for _ in range(M):
    u, v, h = map(int, input().split())
    dp[u-1][v-1] = h
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[i][j] > max(dp[i][k], dp[k][j]):
                dp[i][j] = max(dp[i][k], dp[k][j])
for _ in range(T):
    s, e = map(int, input().split())
    print(dp[s-1][e-1] if dp[s-1][e-1] < INF else -1)