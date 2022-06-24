# https://www.acmicpc.net/problem/16167
# 이름 : A Great Way
# 번호 : 16167
# 난이도 : 골드 III
# 분류 : 그래프 이론, 데이크스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(R):
    a, b, c, d, e = map(int, input().split())
    if e > 10:
        cost = c + d * (e - 10)
    else:
        cost = c
    graph[a].append((cost, b))
heap = [(0, 1, 1)]
dp = [[INF, INF] for _ in range(N + 1)]
dp[1] = [0, 1]
while heap:
    n_dist, k, nx = heappop(heap)
    if dp[nx][0] < n_dist:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if dp[dx][0] > dist:
            dp[dx] = [dist, k + 1]
            heappush(heap, (dist, k + 1, dx))
        elif dp[dx][0] == dist and dp[dx][1] > k + 1:
            dp[dx][1] = k + 1
            heappush(heap, (dist, k + 1, dx))
if dp[N][0] < INF:
    print(*dp[N])
else:
    print('It is not a great way.')