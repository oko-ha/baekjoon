# https://www.acmicpc.net/problem/23087
# 이름 : 최단최단경로
# 번호 : 23087
# 난이도 : 골드 III
# 분류 : 그래프 이론, 데이크스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M, x, y = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
heap = [(0, x)]
dp = [[INF, 0, 1] for _ in range(N + 1)]
dp[x][0] = 0
while heap:
    n_dist, nx = heappop(heap)
    if dp[nx][0] < n_dist:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        j = dp[nx][1] + 1
        k = dp[nx][2]
        if dp[dx][0] > dist:
            dp[dx] = [dist, j, k]
            heappush(heap, (dist, dx))
        elif dp[dx][0] == dist:
            if dp[dx][1] > j:
                dp[dx][1] = j
            elif dp[dx][1] == j:
                dp[dx][2] += k
if dp[y][0] < INF:
    print(dp[y][0])
    print(dp[y][1])
    print(dp[y][2] % (10 ** 9 + 9))
else:
    print(-1)