# https://www.acmicpc.net/problem/23030
# 이름 : 후다다닥을 이겨 츄르를 받자!
# 번호 : 23030
# 난이도 : 골드 IV
# 분류 : 구현, 그래프 이론, 데이크스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
station_num = [0] + list(map(int, input().split()))
M = int(input())
graph = [[[] for _ in range(station_num[i] + 1)] for i in range(N + 1)]
for _ in range(M):
    P1, P2, Q1, Q2 = map(int, input().split())
    graph[P1][P2].append((Q1, Q2))
    graph[Q1][Q2].append((P1, P2))

def dijkstra(t, S1, S2, E1, E2):
    heap = [(0, S1, S2)]
    dp = [[INF] * (station_num[i] + 1) for i in range(N + 1)]
    dp[S1][S2] = 0
    while heap:
        n_dist, n1, n2 = heappop(heap)
        if n1 == E1 and n2 == E2:
            return n_dist
        if dp[n1][n2] < n_dist:
            continue
        for d1, d2 in graph[n1][n2]:
            dist = n_dist + t
            if dp[d1][d2] > dist:
                dp[d1][d2] = dist
                heappush(heap, (dist, d1, d2))
        for i in (1, -1):
            if 0 < n2 + i <= station_num[n1]:
                dist = n_dist + 1
                if dp[n1][n2 + i] > dist:
                    dp[n1][n2 + i] = dist
                    heappush(heap, (dist, n1, n2 + i))
    return -1

K = int(input())
for _ in range(K):
    T, P1, P2, Q1, Q2 = map(int, input().split())
    print(dijkstra(T, P1, P2, Q1, Q2))