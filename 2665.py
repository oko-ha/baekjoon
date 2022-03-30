# https://www.acmicpc.net/problem/2665
# 이름 : 미로만들기
# 번호 : 2665
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라

import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
arr = [list(input().strip()) for _ in range(n)]
visit = [[-1] * n for _ in range(n)]
visit[0][0] = 0
queue = deque([(0, 0, 0)])
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

while queue:
    nx, ny, k = queue.popleft()
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < n and 0 <= y < n:
            if arr[x][y] == '1':
                if visit[x][y] < 0 or visit[x][y] > k:
                    visit[x][y] = k
                    queue.append((x, y, k))
            if arr[x][y] == '0':
                if visit[x][y] < 0 or visit[x][y] > k + 1:
                    visit[x][y] = k + 1
                    queue.append((x, y, k + 1))
print(visit[-1][-1])