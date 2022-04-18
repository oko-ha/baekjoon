# https://www.acmicpc.net/problem/20007
# 이름 : 떡 돌리기
# 번호 : 20007
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M, X, Y = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))
dp = [INF] * N
dp[Y] = 0
heap = [(0, Y)]
while heap:
    n_dist, nx = heappop(heap)
    if dp[nx] < n_dist:
        continue
    for d_dist, dx in graph[nx]:
        dist = n_dist + d_dist
        if dp[dx] > dist:
            dp[dx] = dist
            heappush(heap, (dist, dx))
dp.sort()

def answer():
    ans = 1
    temp = 0
    for d in dp:
        if d > X // 2:
            return -1
        temp += d
        if temp > X // 2:
            ans += 1
            temp = d
    return ans

print(answer())