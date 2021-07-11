# https://www.acmicpc.net/problem/1937
# 이름 : 욕심쟁이 판다
# 번호 : 1937
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
def dfs(nx, ny):
    if dp[nx][ny] < 1:
        dp[nx][ny] = 1
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if graph[x][y] > graph[nx][ny]:
                    dp[nx][ny] = max(dp[nx][ny], dfs(x, y) + 1)
    return dp[nx][ny]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)