# https://www.acmicpc.net/problem/6593
# 이름 : 상범 빌딩
# 번호 : 6593
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
def bfs(a, b, c, arr):
    queue = deque([(a, b, c)])
    dx, dy, dz = [0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]
    while queue:
        nx, ny, nz = queue.popleft()
        for i in range(6):
            x, y, z = nx + dx[i], ny + dy[i], nz + dz[i]
            if 0 <= x < L and 0 <= y < R and 0 <= z < C:
                if arr[x][y][z] == '.':
                    arr[x][y][z] = arr[nx][ny][nz] + 1
                    queue.append((x, y, z))
                elif arr[x][y][z] == 'E':
                    return arr[nx][ny][nz] + 1
    return -1
while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    arr = []
    for _ in range(L):
        arr += [[list(input().strip()) for _ in range(R)]]
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    arr[i][j][k] = 0
                    n = bfs(i, j, k, arr)
                    if n < 0:
                        print('Trapped!')
                    else:
                        print('Escaped in {} minute(s).'.format(n))
                    break