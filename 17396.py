# https://www.acmicpc.net/problem/17396
# 이름 : 백도어
# 번호 : 17396
# 난이도 : 골드 V
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
sight = list(map(int, input().split()))
sight[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    if not sight[a] and not sight[b]:
        graph[a].append((t, b))
        graph[b].append((t, a))
dp = [INF] * N
dp[0] = 0
heap = []
heappush(heap, (0, 0))
while heap:
    dist, nx = heappop(heap)
    if dp[nx] < dist:
        continue
    for n_dist, x in graph[nx]:
        temp = dist + n_dist
        if dp[x] > temp:
            dp[x] = temp
            heappush(heap, (temp, x))
print(dp[-1] if dp[-1] < INF else -1)