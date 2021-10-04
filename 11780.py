# https://www.acmicpc.net/problem/11780
# 이름 : 플로이드 2
# 번호 : 11780
# 난이도 : 골드 III
# 분류 : 그래프 이론, 플로이드-와샬

import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
path = [[[i + 1]] * n for i in range(n)]
for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + path[k][j]
for i in range(n):
    for j in range(n):
        print(graph[i][j] if graph[i][j] < INF else 0, end=' ')
    print()
for i in range(n):
    for j in range(n):
        if 0 < graph[i][j] < INF:
            print(len(path[i][j]) + 1, end=' ')
            print(*path[i][j], end=' ')
            print(j + 1)
        else:
            print(0)