# https://www.acmicpc.net/problem/17141
# 이름 : 연구소 2
# 번호 : 17141
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 브루트포스 알고리즘, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cand = []
empty = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            cand.append((i, j))
            arr[i][j] = 0
            empty += 1
        elif arr[i][j] == 0:
            empty += 1
def bfs():
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visit = [[0] * N for _ in range(N)]
    for vx, vy, t in virus:
        visit[vx][vy] = 1
    cnt = 0
    max_time = 0
    queue = deque(virus)
    while queue:
        nx, ny, time = queue.popleft()
        max_time = max(max_time, time)
        cnt += 1
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N and arr[x][y] == 0 and visit[x][y] == 0:
                visit[x][y] = 1
                queue.append((x, y, time + 1))
    if empty == cnt:
        return max_time
    else:
        return N * N
virus = []
def dfs(k, a):
    global ans
    if k < M:
        for i in range(a, len(cand)):
            virus.append((cand[i]) + (0,))
            dfs(k + 1, i + 1)
            virus.pop()
    else:
        ans = min(bfs(), ans)
ans = N * N
dfs(0, 0)
print(ans if ans < N * N else -1)