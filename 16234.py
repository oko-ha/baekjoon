# https://www.acmicpc.net/problem/16234
# 이름 : 인구 이동
# 번호 : 16234
# 난이도 : 골드 V
# 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0
while True:
    visit = [[-1] * N for _ in range(N)]
    temp = []
    u = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] < 0:
                visit[i][j] = u
                temp.append([arr[i][j], 1])
                queue = deque([(i, j)])
                while queue:
                    nx, ny = queue.popleft()
                    for k in range(4):
                        x, y = nx + dx[k], ny + dy[k]
                        if 0 <= x < N and 0 <= y < N and visit[x][y] < 0:
                            if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                                visit[x][y] = u
                                temp[u][0] += arr[x][y]
                                temp[u][1] += 1
                                queue.append((x, y))
                u += 1
    if N * N == u:
        break
    for i in range(N):
        for j in range(N):
            arr[i][j] = temp[visit[i][j]][0] // temp[visit[i][j]][1]
    ans += 1
print(ans)