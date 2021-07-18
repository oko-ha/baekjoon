# https://www.acmicpc.net/problem/2146
# 이름 : 다리 만들기
# 번호 : 2146
# 난이도 : 골드 III
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def continent(a, b, c):
    queue = deque([(a, b)])
    arr[a][b] = -c
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if arr[x][y] == 1:
                    arr[x][y] = -c
                    queue.append((x, y))
                elif arr[x][y] == 0:
                    arr[x][y] = c
def shore(a, b, c):
    queue = deque([(a, b, 0)])
    visit = set()
    while queue:
        nx, ny, cnt = queue.popleft()
        if (nx, ny) not in visit:
            visit.add((nx, ny))
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < N and 0 <= y < N and arr[x][y] != -c:
                    if arr[x][y] < 0:
                        return cnt + 1
                    else:
                        queue.append((x, y, cnt + 1))
    return float('inf')
ans = float('inf')
cnt = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            continent(i, j, cnt)
            cnt += 1
for k in range(2, cnt + 1):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == k:
                ans = min(ans, shore(i, j, k))
print(ans)