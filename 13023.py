# https://www.acmicpc.net/problem/13023
# 이름 : ABCDE
# 번호 : 13023
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(k, start):
    if k < 5:
        for i in graph[start]:
            if check[i]:
                check[i] = False
                dfs(k + 1, i)
                check[i] = True
    else:
        print(1)
        exit(0)

for i in range(N):
    check = [True] * N
    dfs(0, i)
print(0)