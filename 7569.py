# https://www.acmicpc.net/problem/7569
# 이름 : 토마토
# 번호 : 7569
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
while queue:
    nx, ny, nz = queue.popleft()
    for i in range(6):
        x, y, z = nx+dx[i], ny+dy[i], nz+dz[i]
        if 0 <= x < h and 0 <= y < n and 0 <= z < m:
            if graph[x][y][z] == 0:
                graph[x][y][z] = graph[nx][ny][nz] + 1
                queue.append((x, y, z))
def answer():
    ans = 0
    for i in graph:
        for j in i:
            if 0 in j:
                return -1
            ans = max(max(j), ans)
    return ans - 1
print(answer())