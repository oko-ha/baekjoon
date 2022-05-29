# https://www.acmicpc.net/problem/13911
# 이름 : 집 구하기
# 번호 : 13911
# 난이도 : 골드 II
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

def dijkstra(start, k):
    heap = []
    dp = [INF] * (V + 1)
    for s in start:
        heap.append((0, s))
        dp[s] = 0
    while heap:
        n_dist, nx = heappop(heap)
        if dp[nx] < n_dist:
            continue
        for d_dist, dx in graph[nx]:
            dist = n_dist + d_dist
            if dp[dx] > dist and dist <= k:
                dp[dx] = dist
                heappush(heap, (dist, dx))
    return dp

M, x = map(int, input().split())
Mac = set(map(int, input().split()))
Mdp = dijkstra(Mac, x)
S, y = map(int, input().split())
Star = set(map(int, input().split()))
Sdp = dijkstra(Star, y)
ans = INF
for i in range(1, V + 1):
    if 0 < Mdp[i] < INF and 0 < Sdp[i] < INF:
        ans = min(ans, Mdp[i] + Sdp[i])
print(ans if ans < INF else -1)