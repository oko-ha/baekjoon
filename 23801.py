# https://www.acmicpc.net/problem/23801
# 이름 : 두 단계 최단 경로 2
# 번호 : 23801
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
    graph[v].append((w, u))

def dijkstra(start):
    heap = [(0, start)]
    dp = [INF] * (N + 1)
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

x, z = map(int, input().split())
P = int(input())
x_dijk = dijkstra(x)
z_dijk = dijkstra(z)
ans = INF
for y in map(int, input().split()):
    ans = min(ans, x_dijk[y] + z_dijk[y])
print(ans if ans < INF else -1)