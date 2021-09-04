# https://www.acmicpc.net/problem/1956
# 이름 : 운동
# 번호 : 1956
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 플로이드-와샬

import sys
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
dist = [[INF] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
ans = INF
for i in range(V):
    ans = min(dist[i][i], ans)
print(ans if ans < INF else -1)