# https://www.acmicpc.net/problem/2573
# 이름 : 빙산
# 번호 : 2573
# 난이도 : 골드 IV
# 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
def bfs(a, b):
    queue = deque([(a, b)])
    check[a][b] = 1
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        nx, ny = queue.popleft()
        cnt = 0
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and check[x][y] == 0:
                if arr[x][y] > 0:
                    check[x][y] = 1
                    queue.append((x, y))
                else:
                    cnt += 1
        arr[nx][ny] = max(arr[nx][ny] - cnt, 0)
def melt():
    ans = 0
    while max(map(max, arr)) > 0:
        global check
        check = [[0] * M for _ in range(N)]
        split = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] > 0 and check[i][j] == 0:
                    if split > 0:
                        return ans
                    split = 1
                    bfs(i, j)
        ans += 1
    return 0
print(melt())