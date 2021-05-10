# https://www.acmicpc.net/problem/7576
# 이름 : 토마토
# 번호 : 7576
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue:
    nx, ny = queue.popleft()
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < n and 0 <= y < m:
            if graph[x][y] == 0:
                graph[x][y] = graph[nx][ny] + 1
                queue.append((x, y))
def answer():
    ans = 0
    for g in graph:
        if 0 in g:
            return -1
        ans = max(ans, max(g))
    return ans - 1
print(answer())