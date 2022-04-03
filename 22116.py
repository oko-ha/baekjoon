# https://www.acmicpc.net/problem/22116
# 이름 : 창영이와 퇴근
# 번호 : 22116
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 이분 탐색, 다익스트라, 최소 스패닝 트리

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
heap = [(0, 0, 0)]
dp = [[INF] * N for _ in range(N)]
dp[0][0] = 0
while heap:
    n_slope, nx, ny = heappop(heap)
    if dp[nx][ny] < n_slope:
        continue
    if nx == N - 1 and ny == N - 1:
        print(n_slope)
        break
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < N and 0 <= y < N:
            slope = max(n_slope, abs(arr[nx][ny] - arr[x][y]))
            if dp[x][y] > slope:
                dp[x][y] = slope
                heappush(heap, (slope, x, y))