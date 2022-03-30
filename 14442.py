# https://www.acmicpc.net/problem/14442
# 이름 : 벽 부수고 이동하기 2
# 번호 : 14442
# 난이도 : 골드 III
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
def bfs():
    queue = deque([(0, 0, K)])
    visit = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visit[0][0][K] = 1
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    while queue:
        nx, ny, k = queue.popleft()
        dist = visit[nx][ny][k]
        if nx == N - 1 and ny == M - 1:
            return dist
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and not visit[x][y][k]:
                if not arr[x][y]:
                    visit[x][y][k] = dist + 1
                    queue.append((x, y, k))
                elif k > 0:
                    visit[x][y][k - 1] = dist + 1
                    queue.append((x, y, k - 1))
    return -1
print(bfs())