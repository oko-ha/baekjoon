# https://www.acmicpc.net/problem/1194
# 이름 : 달이 차오른다, 가자.
# 번호 : 1194
# 난이도 : 골드 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 비트마스킹

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
def bfs(a, b):
    queue = deque([(a, b, 0)])
    visit = [[[0] * M for _ in range(N)] for _ in range(2**6)]
    visit[0][a][b] = 1
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        nx, ny, key = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and arr[x][y] != '#' and visit[key][x][y] < 1:
                if arr[x][y] == '1':
                    return visit[key][nx][ny]
                elif arr[x][y] == '.':
                    visit[key][x][y] = visit[key][nx][ny] + 1
                    queue.append((x, y, key))
                elif arr[x][y].isupper():
                    if (1 << ord(arr[x][y]) - 65) & key:
                        visit[key][x][y] = visit[key][nx][ny] + 1
                        queue.append((x, y, key))
                elif arr[x][y].islower():
                    k = (1 << ord(arr[x][y]) - 97) | key
                    visit[k][x][y] = visit[key][nx][ny] + 1
                    queue.append((x, y, k))
    return -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            arr[i][j] = '.'
            print(bfs(i, j))
            break