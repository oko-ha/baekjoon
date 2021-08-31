# https://www.acmicpc.net/problem/11657
# 이름 : 타임머신
# 번호 : 11657
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 벨만-포드

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
def bf(start):
    dp = [float('inf') for _ in range(N + 1)]
    dp[start] = 0
    for i in range(M):
        for node in range(1, N + 1):
            for n_dest, n_dist in graph[node]:
                temp = dp[node] + n_dist
                if dp[n_dest] > temp:
                    if i == M - 1:
                        return -1
                    dp[n_dest] = temp
    return dp[2:]
ans = bf(1)
if ans == -1:
    print(-1)
else:
    for a in ans:
        print(a if a < float('inf') else -1)