# https://www.acmicpc.net/problem/12834
# 이름 : 주간 미팅
# 번호 : 12834
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, V, E = map(int, input().split())
A, B = map(int, input().split())
H = list(map(int, input().split()))
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

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

ans = 0
for h in H:
    dijk = dijkstra(h)
    ans += dijk[A] if dijk[A] < INF else -1
    ans += dijk[B] if dijk[B] < INF else -1
print(ans)