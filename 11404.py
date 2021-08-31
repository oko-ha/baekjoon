# https://www.acmicpc.net/problem/11404
# 이름 : 플로이드
# 번호 : 11404
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 플로이드-와샬

import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
dist = [[INF] * n for _ in range(n)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)
for k in range(n): # 경유지
    dist[k][k] = 0
    for i in range(n): # 출발지
        for j in range(n): # 목적지
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            dist[i][j] = 0
    print(*dist[i])