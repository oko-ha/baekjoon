# https://www.acmicpc.net/problem/13424
# 이름 : 비밀 모임
# 번호 : 13424
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라, 플로이드-와샬

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    K = int(input())
    friends = list(map(int, input().split()))

    def dijkstra(start):
        heap = [(0, start)]
        dp = [INF] * (N + 1)
        dp[start] = 0
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

    F  = []
    for friend in friends:
        F.append(dijkstra(friend))
    F = list(zip(*F))
    ans = [0, INF]
    for i in range(1, N + 1):
        temp = sum(F[i])
        if ans[1] > temp:
            ans[1] = temp
            ans[0] = i
    print(ans[0])