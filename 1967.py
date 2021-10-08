# https://www.acmicpc.net/problem/1967
# 이름 : 트리의 지름
# 번호 : 1967
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))
def dfs(start):
    for i, d in graph[start]:
        if temp[i] < 0:
            temp[i] = temp[start] + d
            dfs(i)
temp = [-1] * n
temp[0] = 0
dfs(0)
m = -1
for i in range(n):
    if temp[i] > m:
        m = temp[i]
        idx = i
temp = [-1] * n
temp[idx] = 0
dfs(idx)
print(max(temp))