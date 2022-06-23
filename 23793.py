# https://www.acmicpc.net/problem/23793
# 이름 : 두 단계 최단 경로 1
# 번호 : 23793
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 데이크스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
x, y, z = map(int, input().split())

def dijkstra(start, k):
    dp = [INF] * (N + 1)
    dp[start] = 0
    heap = [(0, start)]
    while heap:
        n_dist, nx = heappop(heap)
        if dp[nx] < n_dist:
            continue
        for d_dist, dx in graph[nx]:
            if dx == k:
                continue
            dist = n_dist + d_dist
            if dp[dx] > dist:
                dp[dx] = dist
                heappush(heap, (dist, dx))
    return dp

ans = dijkstra(x, 0)[y] + dijkstra(y, 0)[z]
print(ans if ans < INF else -1, end = ' ')
ans = dijkstra(x, y)[z]
print(ans if ans < INF else -1)