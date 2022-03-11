# https://www.acmicpc.net/problem/21736
# 이름 : 헌내기는 친구가 필요해
# 번호 :21736
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]

def bfs(a, b):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = deque([(a, b)])
    campus[a][b] = 'X'
    num = 0
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and campus[x][y] != 'X':  
                if campus[x][y] == 'P':
                    num += 1
                campus[x][y] = 'X'
                queue.append((x, y))
    return num

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            ans = bfs(i, j)
            print(ans if ans > 0 else 'TT')