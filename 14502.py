# https://www.acmicpc.net/problem/14502
# 이름 : 연구소
# 번호 : 14502
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 브루트포스 알고리즘, 너비 우선 탐색

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
cand = []
wall = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        elif arr[i][j] == 0:
            cand.append((i, j))
        else:
            wall += 1
def bfs(arr):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    cnt = 0
    queue = deque(virus)
    while queue:
        nx, ny = queue.popleft()
        cnt += 1
        if cnt > ans:
            break
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and arr[x][y] == 0:
                arr[x][y] = 2
                queue.append((x, y))
    return cnt
def dfs(k, a):
    global ans
    if k < 3:
        for i in range(a, len(cand)):
            x, y = cand[i]
            arr[x][y] = 1
            dfs(k + 1, i + 1)
            arr[x][y] = 0
    else:
        ans = min(bfs(deepcopy(arr)), ans)
ans = N * M - wall - 3
dfs(0, 0)
print(N * M - wall - 3 - ans)