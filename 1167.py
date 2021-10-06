# https://www.acmicpc.net/problem/1167
# 이름 : 트리의 지름
# 번호 : 1167
# 난이도 : 골드 III
# 분류 : 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색

import sys
input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V)]
for _ in range(V):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 2, 2):
        graph[arr[0] - 1].append((arr[i] - 1, arr[i + 1]))
def dfs(start):
    for i, d in graph[start]:
        if temp[i] < 0:
            temp[i] = temp[start] + d
            dfs(i)
temp = [-1] * V
temp[0] = 0
dfs(0)
m = -1
for i in range(V):
    if temp[i] > m:
        m = temp[i]
        idx = i
temp = [-1] * V
temp[idx] = 0
dfs(idx)
print(max(temp))