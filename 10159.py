# https://www.acmicpc.net/problem/10159
# 이름 : 저울
# 번호 : 10159
# 난이도 : 골드 III
# 분류 : 그래프 이론, 그래프 탐색, 플로이드-와샬

import sys
input = sys.stdin.readline

N = int(input())
graph = [[0] * N for _ in range(N)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for i in range(N):
    cnt = 1
    for j in range(N):
        cnt += graph[i][j] + graph[j][i]
    print(N - cnt)