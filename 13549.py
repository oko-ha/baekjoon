# https://www.acmicpc.net/problem/13549
# 이름 : 숨바꼭질 3
# 번호 : 13549
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라, 0-1 너비 우선 탐색

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N, K = map(int, input().split())
def way(x):
    return [(x-1, 1), (x+1, 1), (x*2, 0)] if x < K else [(x-1, 1)]
if N > K:
    print(N - K)
elif N == K:
    print(0)
else:
    INF = sys.maxsize
    dp = [INF] * 100001
    dp[N] = 0
    heap = []
    heappush(heap, [0, N])
    while heap:
        dist, nx = heappop(heap)
        for x, d in way(nx):
            if 0 <= x <= 100000:
                temp = dist + d
                if dp[x] > temp:
                    dp[x] = temp
                    heappush(heap, [temp, x])
    print(dp[K])