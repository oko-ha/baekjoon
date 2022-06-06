# https://www.acmicpc.net/problem/14728
# 이름 : 벼락치기
# 번호 : 14728
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 배낭 문제

import sys
input = sys.stdin.readline

N, T = map(int, input().split())
dp = [[0] * (T + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    K, S  = map(int, input().split())
    for j in range(1, T + 1):
        if j >= K and dp[i - 1][j - K] + S > dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j - K] + S
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])