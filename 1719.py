# https://www.acmicpc.net/problem/1719
# 이름 : 택배
# 번호 : 1719
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라, 플로이드-와샬

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[INF] * N for _ in range(N)]
ans = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
    ans[a-1][b-1] = b
    ans[b-1][a-1] = a
for k in range(N):
    graph[k][k] = 0
    ans[k][k] = '-'
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                ans[i][j] = ans[i][k]
for i in range(N):
    print(*ans[i])