# https://www.acmicpc.net/problem/16946
# 이름 : 벽 부수고 이동하기 4
# 번호 : 16946
# 난이도 : 골드 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
def bfs(a, b):
    queue = deque([(a, b)])
    visit[a][b] = 1
    temp = []
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    cnt = 1
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and not visit[x][y]:
                visit[x][y] = 1
                if arr[x][y] == 0:
                    cnt += 1
                    queue.append((x, y))
                else:
                    temp.append((x, y))
    for x, y in temp:
        visit[x][y] = 0
        arr[x][y] += cnt
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visit[i][j]:
            bfs(i, j)
for ar in arr:
    for a in ar:
        print(a % 10, end='')
    print()