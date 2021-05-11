# https://www.acmicpc.net/problem/7562
# 이름 : 나이트의 이동
# 번호 : 7562
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    graph = [[0 for i in range(n)] for i in range(n)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    graph[a][b] = 1
    queue = deque([(a, b)])
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]
    while queue:
        nx, ny = queue.popleft()
        if nx == c and ny == d:
            print(graph[nx][ny] - 1)
            break
        else:
            for i in range(8):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < n and 0 <= y < n:
                    if graph[x][y] == 0:
                        graph[x][y] = graph[nx][ny] + 1
                        queue.append((x, y))
