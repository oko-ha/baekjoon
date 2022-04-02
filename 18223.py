# https://www.acmicpc.net/problem/18223
# 이름 : 민준이와 마산 그리고 건우
# 번호 : 18223
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

V, E, P = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start):
    heap = [(0, start)]
    dp = [INF] * (V + 1)
    dp[start] = 0
    while heap:
        n_dist, nx = heappop(heap)
        if dp[nx] < n_dist:
            continue
        for d_dist, dx in graph[nx]:
            dist = n_dist + d_dist
            if dp[dx] > dist:
                dp[dx] = dist
                heappush(heap, (dist, dx))
    return dp

dijk_1 = dijkstra(1)
dijk_P = dijkstra(P)
if dijk_1[P] + dijk_P[-1] > dijk_1[-1]:
    print("GOOD BYE")
else:
    print("SAVE HIM")