# https://www.acmicpc.net/problem/5427
# 이름 : 불
# 번호 : 5427
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색-

import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for _ in range(int(input())):
    w, h = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]
    def bfs():
        queue = deque([])
        for i in range(h):
            for j in range(w):
                if arr[i][j] == '@':
                    a, b = i, j
                    arr[i][j] = '#'
                if arr[i][j] == '*':
                    queue.append((i, j, -1))
                    arr[i][j] = '#'
        queue.append((a, b, 0))
        while queue:
            nx, ny, cnt = queue.popleft()
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if cnt < 0:
                    if 0 <= x < h and 0 <= y < w:
                        if arr[x][y] != '*' and arr[x][y] != '#':
                            arr[x][y] = '*'
                            queue.append((x, y, -1))
                else:
                    if 0 <= x < h and 0 <= y < w:
                        if arr[x][y] == '.':
                            arr[x][y] = '#'
                            queue.append((x, y, cnt + 1))
                    else:
                        return cnt + 1
        return 'IMPOSSIBLE'
    print(bfs())