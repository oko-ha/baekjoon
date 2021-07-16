# https://www.acmicpc.net/problem/19238
# 이름 : 스타트 택시
# 번호 : 19238
# 난이도 : 골드 IV
# 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline
N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
texi = [int(i) - 1 for i in input().split()]
direct = {}
for _ in range(M):
    a, b, c, d = map(int, input().split())
    arr[a - 1][b - 1] = 2
    direct[(a - 1, b - 1)] = (c - 1, d - 1)
def find_another(queue, m):
    dir = []
    while queue:
        nx, ny, cnt = queue.popleft()
        if arr[nx][ny] == 2 and cnt == m:
            dir.append((nx, ny))
    return dir
def bfs(a, b, c, d, fuel, flag1):
    queue = deque([(a, b, 0)])
    visit = set()
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    while queue:
        nx, ny, cnt = queue.popleft()
        if flag1 and arr[nx][ny] == 2:
            dir = sorted([(nx, ny)] + find_another(queue, cnt), key=lambda x:(x[0], x[1]))
            d0, d1 = dir[0][0], dir[0][1]
            arr[d0][d1] = 0
            i, j = direct[(d0, d1)]
            return bfs(d0, d1, i, j, fuel - cnt, False)
        if (nx, ny) == (c, d):
            return [c, d], fuel + cnt
        if fuel - cnt <= 0:
            continue
        if (nx, ny) not in visit:
            visit.add((nx, ny))
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < N and 0 <= y < N and arr[x][y] != 1:
                    queue.append((x, y, cnt + 1))
    return 0, -1
for _ in range(M):
    texi, fuel = bfs(texi[0], texi[1], -1, -1, fuel, True)
    if fuel < 0:
        fuel = -1
        break
print(fuel)