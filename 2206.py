# https://www.acmicpc.net/problem/2206
# 이름 : 벽 부수고 이동하기
# 번호 : 2206
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
def bfs():
    queue = deque([(0, 0, 1, 1)])
    visit = set()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        node = queue.popleft()
        nx, ny, c, d = node[0] , node[1], node[2], node[3]
        if (nx, ny, c) not in visit:
            visit.add((nx, ny, c))
            if 0 <= nx < n and 0 <= ny < m:
                if nx == n - 1 and ny == m - 1:
                    return d
                else:
                    for i in range(4):
                        x, y = nx + dx[i], ny + dy[i]
                        if graph[nx][ny] == 0:
                            queue.append((x, y, c, d + 1))
                        elif graph[nx][ny] == 1 and c > 0:
                            queue.append((x, y, c - 1, d + 1))
    return -1
print(bfs())