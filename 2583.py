# https://www.acmicpc.net/problem/2583
# 이름 : 영역 구하기
# 번호 : 2583
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
M, N, K = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x0, y0, x1, y1 = map(int, input().split())
    for i in range(y0, y1):
        for j in range(x0, x1):
            arr[i][j] = 1
def bfs(a, b):
    queue = deque([(a, b)])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    cnt = 0
    while queue:
        nx, ny = queue.popleft()
        if arr[nx][ny] == 0:
            arr[nx][ny] = 1
            cnt += 1
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < M and 0 <= y < N:
                    queue.append((x, y))
    return cnt
ans = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            ans.append(bfs(i, j))
ans.sort()
print(len(ans))
print(*ans)