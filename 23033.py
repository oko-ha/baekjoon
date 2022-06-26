# https://www.acmicpc.net/problem/23033
# 이름 : 집에 빨리 가고 싶어!
# 번호 : 23033
# 난이도 : 골드 III
# 분류 : 그래프 이론, 데이크스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, W = map(int, input().split())
    graph[A - 1].append((T, B - 1, W))
heap = [(0, 0)]
dp = [0] + [INF] * (N - 1)
while heap:
    n_dist, nx = heappop(heap)
    if dp[nx] < n_dist:
        continue
    for d_dist, dx, w in graph[nx]:
        dist = n_dist + d_dist
        if n_dist % w > 0:
            dist += w - (n_dist % w)
        if dp[dx] > dist:
            dp[dx] = dist
            heappush(heap, (dist, dx))
print(dp[-1])