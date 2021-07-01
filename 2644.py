# https://www.acmicpc.net/problem/2644
# 이름 : 촌수계산
# 번호 : 2644
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
graph = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]
def bfs():
    queue = deque([(a, 0)])
    visit = set()
    while queue:
        node, cnt = queue.popleft()
        if node == b:
            return cnt
        if node not in visit:
            visit.add(node)
            for g in graph[node]:
                queue.append((g, cnt + 1))
    return -1
print(bfs())