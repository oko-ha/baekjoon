# https://www.acmicpc.net/problem/13907
# 이름 : 세금
# 번호 : 13907
# 난이도 : 플래티넘 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())
S, D = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))
heap = [(0, S, 0)]
dp = [[INF] * (N + 1) for _ in range(N + 1)]
dp[S][0] = 0
while heap:
    n_dist, nx, k = heappop(heap)
    flag = False
    for i in range(k + 1):
        if dp[nx][i] < n_dist:
            flag = True
            break
    if flag or k == N or nx == D:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if dp[dx][k + 1] > dist:
            dp[dx][k + 1] = dist
            heappush(heap, (dist, dx, k + 1))
print(min(dp[D]))
for _ in range(K):
    n = int(input())
    for i in range(1, N + 1):
        if dp[D][i] < INF:
            dp[D][i] += i * n
    print(min(dp[D]))