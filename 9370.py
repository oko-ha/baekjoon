# https://www.acmicpc.net/problem/9370
# 이름 : 미확인 도착지
# 번호 : 9370
# 난이도 : 골드 II
# 분류 : 그래프 이론, 다익스트라

import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    def dijkstra(start):
        dp = [float('inf') for _ in range(n + 1)]
        dp[start] = 0
        heap = []
        heapq.heappush(heap, [0, start])
        while heap:
            dist, dest = heapq.heappop(heap)
            for n_dest, n_dist in graph[dest]:
                temp = n_dist + dist
                if dp[n_dest] > temp:
                    dp[n_dest] = temp
                    heapq.heappush(heap, [temp, n_dest])
        return dp
    first = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    ans = []
    for _ in range(t):
        x = int(input())
        if min(first[g] + g_[h] + h_[x], first[h] + h_[g] + g_[x]) == first[x] and first[x] < float('inf'):
            ans.append(x)
    print(*sorted(ans))