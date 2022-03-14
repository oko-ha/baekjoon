# https://www.acmicpc.net/problem/5972
# 이름 : 택배 배송
# 번호 : 5972
# 난이도 : 골드 V
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))
dp = [INF] * (N + 1)
dp[1] = 0
heap = []
heappush(heap, [0, 1])
while heap:
    dist, nx = heappop(heap)
    for n_dist, x in graph[nx]:
        temp = dist + n_dist
        if dp[x] > temp:
            dp[x] = temp
            heappush(heap, [temp, x])
print(dp[N])