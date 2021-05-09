# https://www.acmicpc.net/problem/2178
# 이름 : 미로 탐색
# 번호 : 2178
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
visit = []
queue = deque([(0, 0, 0)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue:
    node = queue.popleft()
    nx, ny, dist = node[0], node[1], node[2]
    if (nx, ny) not in visit:
        visit.append((nx, ny))
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1:
                graph[ny][nx] = dist + 1
                for i in range(4):
                    queue.append((nx+dx[i], ny+dy[i], dist+1))
print(graph[-1][-1])