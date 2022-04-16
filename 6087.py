# https://www.acmicpc.net/problem/6087
# 이름 : 레이저 통신
# 번호 : 6087
# 난이도 : 골드 III
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

W, H = map(int, input().split())
arr = [list(input().strip()) for _ in range(H)]

def bfs(a, b):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    heap = [(-1, a, b, -1)]
    visit = [[[INF] * W for _ in range(H)] for _ in range(4)]
    for i in range(4):
        visit[i][a][b] = 0
    while heap:
        mirror, nx, ny, direction = heappop(heap)
        if arr[nx][ny] == 'C':
            return mirror
        if visit[direction][nx][ny] < mirror:
            continue
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < H and 0 <= y < W and arr[x][y] != '*':
                if direction == i:
                    if visit[i][x][y] > mirror:
                        visit[i][x][y] = mirror
                        heappush(heap, (mirror, x, y, direction))
                else:
                    if visit[i][x][y] > mirror + 1:
                        visit[i][x][y] = mirror + 1
                        heappush(heap, (mirror + 1, x, y, i))

def answer():
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'C':
                arr[i][j] = '.'
                return(bfs(i, j))

print(answer())