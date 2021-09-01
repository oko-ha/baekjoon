# https://www.acmicpc.net/problem/1261
# 이름 : 알고스팟
# 번호 : 1261
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라, 0-1 너비 우선 탐색

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(M)]
dp = [[INF] * N for _ in range(M)]
dp[0][0] = 0
heap = []
heappush(heap, [0, 0, 0])
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while heap:
    dist, nx, ny = heappop(heap)
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < M and 0 <= y < N:
            temp = dist + arr[x][y]
            if dp[x][y] > temp:
                dp[x][y] = temp
                heappush(heap, [temp, x, y])
print(dp[M-1][N-1])