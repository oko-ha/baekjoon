# https://www.acmicpc.net/problem/1854
# 이름 : K번째 최단경로 찾기
# 번호 : 1854
# 난이도 : 플래티넘 IV
# 분류 : 그래프 이론, 자료 구조, 다익스트라, 우선순위 큐

import sys
from heapq import heappop, heappush, heappushpop
input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append((c, b-1))
heap = []
heappush(heap, (0, 0))
dp = [[-INF] * k for _ in range(n)]
while heap:
    n_dist, nx = heappop(heap)
    if -dp[nx][0] < n_dist:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if -dp[dx][0] > dist:
            heappushpop(dp[dx], -dist)
            heappush(heap, (dist, dx))
heappushpop(dp[0], 0)
for ans in dp:
    if -ans[0] < INF:
        print(-ans[0])
    else:
        print(-1)