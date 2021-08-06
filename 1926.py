# https://www.acmicpc.net/problem/1926
# 이름 : 그림
# 번호 : 1926
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
def bfs(a, b):
    queue = deque([(a, b)])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    cnt = 1
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
                arr[x][y] = 0
                queue.append((x, y))
                cnt += 1
    return cnt
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 0
            cnt += 1
            ans = max(ans, bfs(i, j))
print(cnt)
print(ans)