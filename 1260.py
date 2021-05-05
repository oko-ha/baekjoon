# https://www.acmicpc.net/problem/1260
# 이름 : DFS와 BFS
# 번호 : 1260
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start):
    visit = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in graph:
                temp = sorted(set(graph[node]), reverse=True)
                stack.extend(temp)
    return visit

def bfs(graph, start):
    visit = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node in graph:
                temp = sorted(set(graph[node]))
                queue.extend(temp)
    return visit

n, m, v = map(int, input().split())
graph = {}
for _ in range(m):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = [y]
    else:
        graph[x].append(y)
    if y not in graph:
        graph[y] = [x]
    else:
        graph[y].append(x)

print(*dfs(graph, v))
print(*bfs(graph, v))