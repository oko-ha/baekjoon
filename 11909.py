# https://www.acmicpc.net/problem/11909
# 이름 : 배열 탈출
# 번호 : 11909
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 다익스트라

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * n for _ in range(n)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        temp_i = temp_j = INF
        if 0 <= i:
            temp_i = dp[i-1][j] + (0 if arr[i][j] < arr[i-1][j] else arr[i][j] - arr[i-1][j] + 1)
        if 0 <= j:
            temp_j = dp[i][j-1] + (0 if arr[i][j] < arr[i][j-1] else arr[i][j] - arr[i][j-1] + 1)
        dp[i][j] = min(temp_i, temp_j)
print(dp[n-1][n-1])