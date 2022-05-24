# https://www.acmicpc.net/problem/1162
# 이름 : 도로포장
# 번호 : 1162
# 난이도 : 골드 I
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append((c, b-1))
    graph[b-1].append((c, a-1))
heap = [(0, 0, K)]
dp = [[0] + [INF] * (N - 1) for _ in range(K + 1)]
while heap:
    n_dist, nx, k = heappop(heap)
    if dp[k][nx] < n_dist:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if dp[k][dx] > dist:
            dp[k][dx] = dist
            heappush(heap, (dist, dx, k))
        if k > 0 and dp[k-1][dx] > n_dist:
            dp[k-1][dx] = n_dist
            heappush(heap, (n_dist, dx, k-1))
print(min(list(zip(*dp))[-1]))