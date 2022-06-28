# https://www.acmicpc.net/problem/23563
# 이름 : 벽 타기
# 번호 : 23563
# 난이도 : 골드 III
# 분류 : 그래프 이론, 데이크스트라, 0-1 너비 우선 탐색

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

H, W = map(int, input().split())
arr = [list(input().strip()) for _ in range(H)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(a, b, c):
    heap = [(0, a, b, c)]
    visit = [[INF] * W for _ in range(H)]
    visit[a][b] = 0
    while heap:
        n_dist, nx, ny, k = heappop(heap)
        if arr[nx][ny] == 'E':
            return n_dist
        if visit[nx][ny] < n_dist:
            continue
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < H and 0 <= y < W and arr[x][y] != '#':
                l = 0
                for j in range(4):
                    wx, wy = x + dx[j], y + dy[j]
                    if 0 <= wx < H and 0 <= wy < W and arr[wx][wy] == '#':
                        l = 1
                        break
                dist = n_dist + 1
                if k and l:
                    dist -= 1
                if visit[x][y] > dist:
                    visit[x][y] = dist
                    heappush(heap, (dist, x, y, l))

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'S':
            l = 0
            for k in range(4):
                if arr[i + dx[k]][j + dy[k]] == '#':
                    l = 1
                    break
            print(bfs(i, j, l))