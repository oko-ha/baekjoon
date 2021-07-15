# https://www.acmicpc.net/problem/2468
# 이름 : 안전 영역
# 번호 : 2468
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 브루트포스 알고리즘, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
def bfs(a, b):
    queue = deque([(a, b)])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if temp[x][y] == 0 and arr[x][y] > k:
                    temp[x][y] = 1
                    queue.append((x, y))
ans = 1
for k in range(min(map(min, arr)), max(map(max, arr)) + 1):
    cnt = 0
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 0 and arr[i][j] > k:
                temp[i][j] = 1
                bfs(i, j)
                cnt += 1
    ans = max(cnt, ans)
print(ans)