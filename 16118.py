# https://www.acmicpc.net/problem/16118
# 이름 : 달빛 여우
# 번호 : 16118
# 난이도 : 골드 I
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a-1].append((d, b-1))
    graph[b-1].append((d, a-1))

def dijkstra_fox():
    fox = [0] + [INF] * (N - 1)
    heap = []
    heappush(heap, (0, 0))
    while heap:
        n_dist, nx = heappop(heap)
        if fox[nx] < n_dist:
            continue
        for d_dist, dx in graph[nx]:
            dist = n_dist + d_dist
            if fox[dx] > dist:
                fox[dx] = dist
                heappush(heap, (dist, dx))
    return fox

def dijkstra_wolf():
    wolf = [[INF, INF] for _ in range(N)]
    wolf[0][0] = 0
    heap = []
    heappush(heap, (0, 0, 0))
    while heap:
        n_dist, nx, rush = heappop(heap)
        if wolf[nx][rush] < n_dist:
            continue
        rush ^= 1
        for d_dist, dx in graph[nx]:
            dist = d_dist / 2 + n_dist if rush else d_dist * 2 + n_dist
            if wolf[dx][rush] > dist:
                wolf[dx][rush] = dist
                heappush(heap, (dist, dx, rush))
    
    return wolf

f = dijkstra_fox()
w = dijkstra_wolf()
ans = 0
for i in range(1, N):
    if f[i] < min(w[i]):
        ans += 1
print(ans)