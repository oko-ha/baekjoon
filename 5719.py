# https://www.acmicpc.net/problem/5719
# 이름 : 거의 최단 경로
# 번호 : 5719
# 난이도 : 플래티넘 V
# 분류 : 그래프 이론, 그래프 탐색, 다익스트라

import sys
from heapq import heappop, heappush
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    inv_graph = [[] for _ in range(N)]
    shortest_path = [[0] * N for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U].append((P, V))
        inv_graph[V].append((P, U))

    def dijkstra():
        heap = [(0, S)]
        dp = [INF] * N
        dp[S] = 0
        while heap:
            n_dist, nx = heappop(heap)
            if dp[nx] < n_dist:
                continue
            for d_dist, dx in graph[nx]:
                if not shortest_path[nx][dx]:  
                    dist = n_dist + d_dist
                    if dp[dx] > dist:
                        dp[dx] = dist
                        heappush(heap, (dist, dx))
        return dp

    def bfs(dp):
        queue = deque([D])
        while queue:
            nx = queue.popleft()
            if nx == S:
                continue
            for dist, dx in inv_graph[nx]:
                if dp[nx] == dp[dx] + dist and not shortest_path[dx][nx]:
                    shortest_path[dx][nx] = 1
                    queue.append(dx)

    dist = dijkstra()
    bfs(dist)
    dist = dijkstra()
    print(dist[D] if dist[D] < INF else -1)