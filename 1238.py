# https://www.acmicpc.net/problem/1238
# 이름 : 파티
# 번호 : 1238
# 난이도 : 골드 III
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
N, M, X = map(int, input().split())
f_graph = [[] for _ in range(N)]
r_graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, T = map(int, input().split())
    f_graph[A - 1].append((T, B - 1))
    r_graph[B - 1].append((T, A - 1))
def dijkstra(graph):
    dp = [INF] * N
    dp[X - 1] = 0
    heap = []
    heappush(heap, [0, X - 1])
    while heap:
        dist, dest = heappop(heap)
        for n_dist, n_dest in graph[dest]:
            temp = dist + n_dist
            if dp[n_dest] > temp:
                dp[n_dest] = temp
                heappush(heap, [temp, n_dest])
    return dp
ans = 0
forward = dijkstra(f_graph)
reverse = dijkstra(r_graph)
for i in range(N):
    ans = max(forward[i] + reverse[i], ans)
print(ans)