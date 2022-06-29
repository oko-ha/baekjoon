# https://www.acmicpc.net/problem/14221
# 이름 : 편의점
# 번호 : 14221
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 데이크스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
p, q = map(int, input().split())
pp = sorted(list(map(int, input().split())))
qq = list(map(int, input().split()))

def dijkstra():
    heap = []
    dp = [INF] * (n + 1)
    for qqq in qq:
        heap.append((0, qqq))
        dp[qqq] = 0
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

d = dijkstra()
ans = [INF, 0]
for ppp in pp:
    if ans[0] > d[ppp]:
        ans[0] = d[ppp]
        ans[1] = ppp
print(ans[1])