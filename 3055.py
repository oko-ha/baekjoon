# https://www.acmicpc.net/problem/3055
# 이름 : 탈출
# 번호 : 3055
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
q = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            q.append((i, j, 0))
        if arr[i][j] == 'S':
            temp = (i, j, 0)
q.append(temp)
def bfs(q):
    queue = deque(q)
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        nx, ny, cnt = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < R and 0 <= y < C:
                if arr[nx][ny] == 'S':
                    if arr[x][y] == '.':
                        arr[x][y] = 'S'
                        queue.append((x, y, cnt + 1))
                    elif arr[x][y] == 'D':
                        return cnt + 1
                elif arr[nx][ny] == '*':
                    if arr[x][y] == '.':
                        arr[x][y] = '*'
                        queue.append((x, y, cnt + 1))
    return 'KAKTUS'
print(bfs(q))