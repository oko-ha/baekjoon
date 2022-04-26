# https://www.acmicpc.net/problem/2458
# 이름 : 키 순서
# 번호 : 2458
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 플로이드-와샬

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
ans = 0
for i in range(N):
    cnt = 1
    for j in range(N):
        cnt += graph[i][j] + graph[j][i]
    if cnt == N:
        ans += 1
print(ans)