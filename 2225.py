# https://www.acmicpc.net/problem/2225
# 이름 : 합분해
# 번호 : 2225
# 난이도 : 골드 V
# 분류 : 수학, 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[1] * N for _ in range(K)]
for i in range(1, K):
    dp[i][0] = i + 1
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1] % 1000000000)