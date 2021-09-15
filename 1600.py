# https://www.acmicpc.net/problem/1600
# 이름 : 말이 되고픈 원숭이
# 번호 : 1600
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visit = [[[-1] * W for _ in range(H)] for _ in range(K + 1)]
visit[0][0][0] = 0
queue = deque([(0, 0, 0)])
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
dhx, dhy = [1, 1, 2, 2, -1, -1, -2, -2], [2, -2, 1, -1, 2, -2, 1, -1]
ans = -1
while queue:
    nx, ny, cnt = queue.popleft()
    if nx == H - 1 and ny == W - 1:
        ans = visit[cnt][nx][ny]
        break
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < H and 0 <= y < W:
            if arr[x][y] < 1 and visit[cnt][x][y] < 0:
                visit[cnt][x][y] = visit[cnt][nx][ny] + 1
                queue.append((x, y, cnt))
    if cnt < K:
        for i in range(8):
            x, y = nx + dhx[i], ny + dhy[i]
            if 0 <= x < H and 0 <= y < W:
                if arr[x][y] < 1 and visit[cnt + 1][x][y] < 0:
                    visit[cnt + 1][x][y] = visit[cnt][nx][ny] + 1
                    queue.append((x, y, cnt + 1))
print(ans)