# https://www.acmicpc.net/problem/1012
# 이름 : 유기농 배추
# 번호 : 1012
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    visit = []
    queue = deque([(x, y)])
    while queue:
        node = queue.popleft()
        nx = node[0]
        ny = node[1]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx - 1, ny))
                queue.append((nx, ny - 1))
                queue.append((nx + 1, ny))
                queue.append((nx, ny + 1))

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)