# https://www.acmicpc.net/problem/14499
# 이름 : 주사위 굴리기
# 번호 : 14499
# 난이도 : 골드 IV
# 분류 : 구현, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dice = [deque([0, 0, 0, 0]), 0, 0]
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
def roll_dice():
    temp = dice[0][0]
    dice[0][0] = dice[2]
    dice[2] = dice[0][2]
    dice[0][2] = dice[1]
    dice[1] = temp
for i in list(map(int, input().split())):
    x, y = x + dx[i], y + dy[i]
    if 0 <= x < N and 0 <= y < M:
        if i < 3:
            temp = dice[0][0]
            dice[0][0] = dice[i]
            dice[i] = dice[0][2]
            dice[0][2] = dice[3 - i]
            dice[3 - i] = temp
        elif i == 3:
            dice[0].rotate(-1)
        else:
            dice[0].rotate(1)
        if arr[x][y] == 0:
            arr[x][y] = dice[0][2]
        else:
            dice[0][2] = arr[x][y]
            arr[x][y] = 0
        print(dice[0][0])  
    else:
        x, y = x - dx[i], y - dy[i]