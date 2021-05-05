# https://www.acmicpc.net/problem/2606
# 이름 : 바이러스
# 번호 : 2606
# 난이도 : 실버 III
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {}
for _ in range(m):
    x, y = map(int, input().split())
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]
visit = []
stack = [1]
while stack:
    node = stack.pop()
    if node not in visit:
        visit.append(node)
        if node in graph:
            stack.extend(set(graph[node]))
print(len(visit) - 1)