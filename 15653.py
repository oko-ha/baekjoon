# https://www.acmicpc.net/problem/15653
# 이름 : 구슬 탈출 4
# 번호 : 15653
# 난이도 : 골드 II
# 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
q = []
def find_ball():
    rFlag = bFlag = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                arr[i][j] = '.'
                R = (i, j)
                rFlag = True
            elif arr[i][j] == 'B':
                arr[i][j] = '.'
                B = (i, j)
                bFlag = True
            if rFlag and bFlag:
                return (R + B + (0,))
q.append(find_ball())
def bfs(q):
    queue = deque(q)
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visit = set()
    while queue:
        rnx, rny, bnx, bny, cnt = queue.popleft()
        if (rnx, rny, bnx, bny) not in visit:
            visit.add((rnx, rny, bnx, bny))
            for i in range(4):
                rx, ry, r, bx, by, b = rnx, rny, 0, bnx, bny, 0
                while arr[rx + dx[i]][ry + dy[i]] == '.':
                    rx += dx[i]
                    ry += dy[i]
                    r += 1
                while arr[bx + dx[i]][by + dy[i]] == '.':
                    bx += dx[i]
                    by += dy[i]
                    b += 1
                if arr[bx + dx[i]][by + dy[i]] == 'O':
                    continue
                if arr[rx + dx[i]][ry + dy[i]] == 'O':
                    return cnt + 1
                if rx == bx and ry == by:
                    if r > b:
                        rx -= dx[i]
                        ry -= dy[i]
                    elif r < b:
                        bx -= dx[i]
                        by -= dy[i]
                queue.append((rx, ry, bx, by, cnt + 1))
    return -1
print(bfs(q))