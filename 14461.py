# https://www.acmicpc.net/problem/14461
# 이름 : 소가 길을 건너간 이유 7
# 번호 : 14461
# 난이도 : 골드 II
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[[INF] * 3 for _ in range(N)] for _ in range(N)]
visit[0][0] = [0, 0, 0]
heap = [(0, 0, 0, 0)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while heap:
    n_dist, k, nx, ny = heappop(heap)
    if nx == N - 1 and ny == N - 1:
        print(n_dist)
        break
    if visit[nx][ny][k] < n_dist:
        continue
    k = (k + 1) % 3
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < N and 0 <= y < N:
            dist = n_dist + T
            if k == 0:
                dist += arr[x][y]
            if visit[x][y][k] > dist:
                visit[x][y][k] = dist
                heappush(heap, (dist, k, x, y))