# https://www.acmicpc.net/problem/11779
# 이름 : 최소비용 구하기 2
# 번호 : 11779
# 난이도 : 골드 III
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
dp = [INF] * (n + 1)
path = [[] for _ in range(n + 1)]
dp[start] = 0
heap = []
heappush(heap, (start, 0, [start]))
while heap:
    nx, nd, p = heappop(heap)
    if dp[nx] < nd:
        continue
    for dx, dd in graph[nx]:
        dist = nd + dd
        if dp[dx] > dist:
            dp[dx] = dist
            path[dx] = p + [dx]
            heappush(heap, (dx, dist, p + [dx]))
print(dp[end])
print(len(path[end]))
print(*path[end])