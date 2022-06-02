# https://www.acmicpc.net/problem/14503
# 이름 : 로봇 청소기
# 번호 : 14503
# 난이도 : 골드 V
# 분류 : 구현, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque([(r, c, d)])
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
arr[r][c] = 2
ans = 1
while queue:
    nx, ny, nd = queue.popleft()
    flag = True
    for i in range(1, 5):
        d = (nd - i) % 4
        x, y = nx + dx[d], ny + dy[d]
        if arr[x][y] == 0:
            arr[x][y] = 2
            queue.append((x, y, d))
            ans += 1
            flag = False
            break
    if flag:
        d = (nd + 2) % 4
        x, y = nx + dx[d], ny + dy[d]
        if arr[x][y] != 1:
            queue.append((x, y, nd))
        else:
            print(ans)
            break