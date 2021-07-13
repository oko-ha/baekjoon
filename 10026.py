# https://www.acmicpc.net/problem/10026
# 이름 : 적록색약
# 번호 : 10026
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
pic = [list(input().rstrip()) for _ in range(N)]
check1 = [[0 for _ in range(N)] for _ in range(N)]
check2 = [[0 for _ in range(N)] for _ in range(N)]
def bfs(a, b, check, flag):
    queue = deque([(a, b)])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        nx, ny = queue.popleft()
        if check[nx][ny] == 0:
            check[nx][ny] = 1
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < N and 0 <= y < N:
                    if flag:
                        if pic[nx][ny] == pic[x][y]:
                            queue.append((x, y))
                    else:
                        if pic[nx][ny] == 'B' and pic[x][y] == 'B':
                            queue.append((x, y))
                        elif pic[nx][ny] != 'B' and pic[x][y] != 'B':
                            queue.append((x, y))
ans = [0, 0]
for i in range(N):
    for j in range(N):
        if check1[i][j] == 0:
            ans[0] += 1
            bfs(i, j, check1, True)
        if check2[i][j] == 0:
            ans[1] += 1
            bfs(i, j, check2, False)
print(*ans)