# https://www.acmicpc.net/problem/1520
# 이름 : 내리막 길
# 번호 : 1520
# 난이도 : 골드 IV
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def dfs(nx, ny):
    if nx == M - 1 and ny == N - 1:
        return 1
    if dp[nx][ny] > -1:
        return dp[nx][ny]
    dp[nx][ny] = 0
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < M and 0 <= y < N and arr[nx][ny] > arr[x][y]:
            dp[nx][ny] += dfs(x, y)
    return dp[nx][ny]
print(dfs(0, 0))