# https://www.acmicpc.net/problem/2307
# 이름 : 도로검문
# 번호 : 2307
# 난이도 : 골드 II
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a-1].append((t, b-1))
    graph[b-1].append((t, a-1))

def dijkstra(a, b):
    heap = [(0, 0)]
    dp = [0] + [INF] * (N - 1)
    while heap:
        n_dist, nx = heappop(heap)
        if dp[nx] < n_dist:
            continue
        for d_dist, dx in graph[nx]:
            if a == nx and b == dx:
                continue
            dist = n_dist + d_dist
            if dp[dx] > dist:
                dp[dx] = dist
                heappush(heap, (dist, dx))
    return dp

dp = dijkstra(-1, -1)
ans = -1
queue = deque([N - 1])
while queue:
    nx = queue.popleft()
    if nx == 0:
        continue
    for dist, dx in graph[nx]:
        if dp[nx] == dp[dx] + dist:
            ans = max(ans, dijkstra(dx, nx)[-1])
            queue.append(dx)
if ans < INF:
    print(ans - dp[-1])
else:
    print(-1)