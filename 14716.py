# https://www.acmicpc.net/problem/14716
# 이름 : 현수막
# 번호 : 14716
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dx, dy = [0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(a, b):
    queue = deque([(a, b)])
    arr[a][b] = 0
    while queue:
        nx, ny = queue.popleft()
        for i in range(8):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < M and 0 <= y < N and arr[x][y]:
                arr[x][y] = 0
                queue.append((x, y))
    return 1

ans = 0
for i in range(M):
    for j in range(N):
        if arr[i][j]:
            ans += bfs(i, j)
print(ans)