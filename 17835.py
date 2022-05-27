# https://www.acmicpc.net/problem/17835
# 이름 : 면접보는 승범이네
# 번호 : 17835
# 난이도 : 골드 II
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    U, V, C = map(int, input().split())
    graph[V].append((C, U))
heap = []
dp = [INF] * (N + 1)
for i in map(int, input().split()):
    heap.append((0, i))
    dp[i] = 0
while heap:
    n_dist, nx = heappop(heap)
    if dp[nx] < n_dist:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if dp[dx] > dist:
            dp[dx] = dist
            heappush(heap, (dist, dx))
ans = [0, 0]
for i in range(1, N + 1):
    if dp[i] > ans[1]:
        ans = [i, dp[i]]
for a in ans:
    print(a)