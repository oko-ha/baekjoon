# https://www.acmicpc.net/problem/18352
# 이름 : 특정 거리의 도시 찾기
# 번호 : 18352
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append((1, B-1))
dp = [INF] * N
dp[X-1] = 0
heap = []
heappush(heap, (0, X-1))
while heap:
    n_dist, nx = heappop(heap)
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if dp[dx] > dist:
            dp[dx] = dist
            heappush(heap, (dist, dx))
flag = True
for i in range(N):
    if dp[i] == K:
        print(i + 1)
        flag = False
if flag:
    print(-1)