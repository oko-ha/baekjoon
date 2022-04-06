# https://www.acmicpc.net/problem/17404
# 이름 : RGB거리 2
# 번호 : 17404
# 난이도 : 골드 IV
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = INF
for i in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][i] = arr[0][i]
    for j in range(1, N):
        dp[j][0] = arr[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = arr[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = arr[j][2] + min(dp[j-1][0], dp[j-1][1])
    for j in range(3):
        if i == j:
            continue
        ans = min(ans, dp[-1][j])
print(ans)