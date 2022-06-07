# https://www.acmicpc.net/problem/2631
# 이름 : 줄세우기
# 번호 : 2631
# 난이도 : 골드 IV
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        if i + 1 == arr[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(N - dp[-1][-1])