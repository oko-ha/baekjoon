# https://www.acmicpc.net/problem/10217
# 이름 : KCM Travel
# 번호 : 10217
# 난이도 : 골드 I
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 다익스트라

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
for _ in range(int(input())):
    def dijkstra():
        N, M, K = map(int, input().split())
        graph = [[] for _ in range(N + 1)]
        for _ in range(K):
            u, v, c, d = map(int, input().split())
            graph[u-1].append((d, v-1, c))
        dp = [[INF] * (M + 1) for _ in range(N)]
        dp[0][0] = 0
        heap = []
        heappush(heap, [0, 0, 0])
        while heap:
            nd, nx, nc = heappop(heap)
            if nx == N-1:
                return nd
            if dp[nx][nc] < nd:
                continue
            for dd, dx, dc in graph[nx]:
                dist = dd + nd
                cost = dc + nc                
                if cost <= M and dp[dx][cost] > dist:
                    for i in range(cost, M + 1):
                        if dp[dx][i] > dist:
                            dp[dx][i] = dist
                        else:
                            break
                    heappush(heap, [dist, dx, cost])
        return 'Poor KCM'
    print(dijkstra())