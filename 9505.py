# https://www.acmicpc.net/problem/9505
# 이름 : 엔터프라이즈호 탈출
# 번호 : 9505
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    K, W, H = map(int, input().split())
    graph = {'E' : 0}
    for _ in range(K):
        k, t = input().split()
        graph[k] = int(t)
    arr = [list(input().strip()) for _ in range(H)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    def bfs(a, b):
        heap = [(0, a, b)]
        dp = [[INF] * W for _ in range(H)]
        dp[a][b] = 0
        while heap:
            nt, nx, ny = heappop(heap)
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < H and 0 <= y < W:
                    t = nt + graph[arr[x][y]]
                    if dp[x][y] > t:
                        dp[x][y] = t
                        heappush(heap, (t, x, y))
                else:
                    return dp[nx][ny]

    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'E':
                print(bfs(i, j))