# https://www.acmicpc.net/problem/16948
# 이름 : 데스 나이트
# 번호 : 16948
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
def bfs():
    dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
    arr = [[-1] * N for _ in range(N)]
    arr[r1][c1] = 0
    queue = deque([(r1, c1)])
    while queue:
        nx, ny = queue.popleft()
        if nx == r2 and ny == c2:
            return arr[nx][ny]
        for i in range(6):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < N and arr[x][y] == -1:
                arr[x][y] = arr[nx][ny] + 1
                queue.append((x, y))
    return -1
print(bfs())