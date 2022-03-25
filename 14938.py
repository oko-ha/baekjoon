# https://www.acmicpc.net/problem/14938
# 이름 : 서강그라운드
# 번호 : 14938
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라, 플로이드-와샬

import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
dist = [[INF] * n for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a-1][b-1] = l
    dist[b-1][a-1] = l
for k in range(n):
    dist[k][k] = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
ans = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if dist[i][j] <= m:
            temp += items[j]
    ans = max(ans, temp)
print(ans)