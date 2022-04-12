# https://www.acmicpc.net/problem/22865
# 이름 : 가장 먼 곳
# 번호 : 22865
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
A, B, C = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append((L, E))
    graph[E].append((L, D))

def dijkstra(start):
    heap = [(0, start)]
    dp = [INF] * (N + 1)
    dp[start] = dp[0] = 0
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
m = 0
dijk_A = dijkstra(A)
dijk_B = dijkstra(B)
dijk_C = dijkstra(C)
for i in range(1, N + 1):
    temp = min(dijk_A[i], dijk_B[i], dijk_C[i])
    if m < temp:
        m = temp
        ans = i
print(ans)