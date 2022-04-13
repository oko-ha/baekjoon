# https://www.acmicpc.net/problem/2589
# 이름 : 보물섬
# 번호 : 2589
# 난이도 : 골드 V
# 분류 : 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(a, b):
    queue = deque([(a, b, 0)])
    visit = [[0] * M for _ in range(N)]
    visit[a][b] = 1
    dist = 0
    while queue:
        nx, ny, d = queue.popleft()
        dist = max(dist, d)
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and arr[x][y] == 'L' and not visit[x][y]:
                visit[x][y] = 1
                queue.append((x, y, d + 1))
    return dist

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans)