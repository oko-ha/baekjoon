# https://www.acmicpc.net/problem/16958
# 이름 : 텔레포트
# 번호 : 16958
# 난이도 : 골드 V
# 분류 : 그래프 이론, 브루트포스 알고리즘, 플로이드-와샬

import sys
input = sys.stdin.readline

N, T = map(int, input().split())
city = []
for _ in range(N):
    city.append(tuple(map(int, input().split())))
dist = [[2000] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = abs(city[i][1] - city[j][1]) + abs(city[i][2] - city[j][2])
            if city[i][0] and city[j][0] and dist[i][j] > T:
                dist[i][j] = T
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
for _ in range(int(input())):
    A, B = map(int, input().split())
    print(dist[A-1][B-1])