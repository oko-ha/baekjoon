# https://www.acmicpc.net/problem/20926
# 이름 : 얼음 미로
# 번호 : 20926
# 난이도 : 골드 II
# 분류 : 구현, 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

W, H = map(int, input().split())
arr = [list(input().strip()) for _ in range(H)]

def bfs(a, b):
    heap = [(0, a, b)]
    dp = [[INF] * W for _ in range(H)]
    dp[a][b] = 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while heap:
        nt, nx, ny= heappop(heap)
        if arr[nx][ny] == 'E':
            return nt
        if dp[nx][ny] < nt:
            continue
        for i in range(4):
            x, y, t = nx + dx[i], ny + dy[i], nt
            while 0 <= x < H and 0 <= y < W and arr[x][y] != 'H':
                if arr[x][y] == 'R':
                    x, y = x - dx[i], y - dy[i]
                    if dp[x][y] > t:
                        dp[x][y] = t
                        heappush(heap, (t, x, y))
                    break
                elif arr[x][y] == 'E':
                    if dp[x][y] > t:
                        dp[x][y] = t
                        heappush(heap, (t, x, y))
                    break
                else:
                    t += int(arr[x][y])
                    x, y = x + dx[i], y + dy[i]
    return -1

def answer():
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'T':
                arr[i][j] = '0'
                return bfs(i, j)

print(answer())