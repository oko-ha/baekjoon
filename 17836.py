# https://www.acmicpc.net/problem/17836
# 이름 : 공주님을 구해라!
# 번호 : 17836
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
def bfs():
    if arr[0][0] == 2:
        gramr = True
    else:
        gramr = False
    queue = deque([(0, 0, 0, gramr)])
    visit = set()
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        nx, ny, cnt, gramr = queue.popleft()
        if (nx, ny, gramr) not in visit:
            visit.add((nx, ny, gramr))
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < N and 0 <= y < M and cnt < T:
                    if x == N - 1 and y == M - 1:
                        return cnt + 1
                    if arr[x][y] == 0:
                        queue.append((x, y, cnt + 1, gramr))
                    elif arr[x][y] == 1 and gramr:
                        queue.append((x, y, cnt + 1, gramr))
                    elif arr[x][y] == 2:
                        queue.append((x, y, cnt + 1, True))
    return 'Fail'
print(bfs())