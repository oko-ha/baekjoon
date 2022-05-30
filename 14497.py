# https://www.acmicpc.net/problem/14497
# 이름 : 주난의 난(難)
# 번호 : 14497
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

def dijkstra():
    visit = [[INF] * M for _ in range(N)]
    visit[x1-1][y1-1] = 0
    heap = [(0, x1-1, y1-1)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while heap:
        n_dist, nx, ny = heappop(heap)
        if visit[nx][ny] < n_dist:
            continue
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == '#':
                    return n_dist + 1
                elif arr[x][y] == '*':
                    continue
                elif visit[x][y] > n_dist + int(arr[x][y]):
                    visit[x][y] = n_dist + int(arr[x][y])
                    heappush(heap, (visit[x][y], x, y))

print(dijkstra())