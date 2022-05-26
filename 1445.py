# https://www.acmicpc.net/problem/1445
# 이름 : 일요일 아침의 데이트
# 번호 : 1445
# 난이도 : 골드 II
# 분류 : 그래프 이론, 자료 구조, 다익스트라, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
temp = [list(input().strip()) for _ in range(N)]
arr = [[0] * M for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visit = [[0] * M for _ in range(N)]
heap = []
for i in range(N):
    for j in range(M):
        if temp[i][j] == 'g':
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < N and 0 <= y < M and not arr[x][y]:
                    arr[x][y] = 1
            arr[i][j] = 2
        elif temp[i][j] == 'F':
            arr[i][j] = 3
        elif temp[i][j] == 'S':
            heappush(heap, (0, 0, i, j))
            visit[i][j] = 1
while heap:
    a, b, nx, ny = heappop(heap)
    if arr[nx][ny] == 3:
        print(a, b)
        break
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < N and 0 <= y < M and not visit[x][y]:
            visit[x][y] = 1
            if arr[x][y] == 0:
                heappush(heap, (a, b, x, y))
            elif arr[x][y] == 1:
                heappush(heap,(a, b + 1, x, y))
            elif arr[x][y] == 2:
                heappush(heap,(a + 1, b, x, y))
            else:
                heappush(heap, (a, b, x, y))