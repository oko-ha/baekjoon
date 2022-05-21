# https://www.acmicpc.net/problem/2660
# 이름 : 회장뽑기
# 번호 : 2660
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-와샬

import sys
input = sys.stdin.readline

N = int(input())
graph = [[N] * (N + 1) for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1, N + 1):
    graph[k][k] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
score = list(map(max, *graph[1:]))
min_score = min(score)
ans = []
for i in range(N + 1):
    if score[i] == min_score:
        ans.append(i)
print(min_score, len(ans))
print(*ans)