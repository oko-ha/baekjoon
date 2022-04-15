# https://www.acmicpc.net/problem/16954
# 이름 : 움직이는 미로 탈출
# 번호 : 16954
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(8)]

def bfs():
    dx, dy = [0, 0, 0, 1, -1, 1, 1, -1, -1], [0, 1, -1, 0, 0, 1, -1, 1, -1]
    queue = deque([(7, 0)])
    visit = [[0] * 8 for _ in range(8)]
    while queue:
        nx, ny = queue.popleft()
        if nx == 0:
            return 1
        for i in range(9):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < 8 and 0 <= y < 8 and not visit[x - 1][y]:
                if arr[x][y] == '.' and arr[x - 1][y] == '.':
                    visit[x - 1][y] = 1
                    queue.append((x - 1, y))
    return 0

print(bfs())