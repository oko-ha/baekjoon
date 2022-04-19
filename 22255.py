# https://www.acmicpc.net/problem/22255
# 이름 : 호석사우루스
# 번호 : 22255
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
Sx, Sy, Ex, Ey = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def dijkstra():
    heap = [(0, Sx - 1, Sy - 1, 1)]
    dp = [[[INF] * M for _ in range(N)] for _ in range(3)]
    dp[1][Sx - 1][Sy - 1] = 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while heap:
        n_impulse, nx, ny, n_turn = heappop(heap)
        if dp[n_turn][nx][ny] < n_impulse:
            continue
        for i in range(4):
            if n_turn == 1 and i < 2:
                continue
            elif n_turn == 2 and i > 1:
                continue
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M and arr[x][y] != -1:
                if x == Ex - 1 and y == Ey - 1:
                    return n_impulse
                impulse = n_impulse + arr[x][y]
                turn = (n_turn + 1) % 3
                if dp[turn][x][y] > impulse:
                    dp[turn][x][y] = impulse
                    heappush(heap, (impulse, x, y, turn))
    return -1
        
print(dijkstra())