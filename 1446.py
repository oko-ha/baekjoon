# https://www.acmicpc.net/problem/1446
# 이름 : 지름길
# 번호 : 1446
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, D = map(int, input().split())
graph = [[(1, i + 1)] for i in range(D)]
for _ in range(N):
    a, b, c = map(int, input().split())
    if b <= D and b - a > c:
        graph[a].append((c, b))
heap = [(0, 0)]
dp = [0] + [INF] * D
while heap:
    n_dist, nx = heappop(heap)
    if nx == D:
        break
    if dp[nx] < n_dist:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if dp[dx] > dist:
            dp[dx] = dist
            heappush(heap, (dist, dx))
print(dp[D])