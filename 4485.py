# https://www.acmicpc.net/problem/4485
# 이름 : 녹색 옷 입은 애가 젤다지?
# 번호 : 4485
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
index = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[INF] * N for _ in range(N)]
    dp[0][0] = 0
    heap = []
    heappush(heap, [0, 0, 0])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while heap:
        dist, nx, ny = heappop(heap)
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N:
                temp = dist + graph[nx][ny]
                if dp[x][y] > temp:
                    dp[x][y] = temp
                    heappush(heap, [temp, x, y])
    print('Problem {}: {}'.format(index, dp[N-1][N-1] + graph[N-1][N-1]))
    index += 1