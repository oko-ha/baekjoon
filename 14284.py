# https://www.acmicpc.net/problem/14284
# 이름 : 간선 이어가기 2
# 번호 : 14284
# 난이도 : 골드 V
# 분류 : 그래프 이론, 데이크스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start, end):
    heap = [(0, start)]
    dp = [INF] * (n + 1)
    dp[start] = 0
    while heap:
        n_dist, nx = heappop(heap)
        if nx == end:
            return n_dist
        if dp[nx] < n_dist:
            continue
        for d_dist, dx in graph[nx]:
            dist = n_dist + d_dist
            if dp[dx] > dist:
                dp[dx] = dist
                heappush(heap, (dist, dx))

s, t = map(int, input().split())
print(dijkstra(s, t))