# https://www.acmicpc.net/problem/16919
# 이름 : 봄버맨 2
# 번호 : 16918
# 난이도 : 골드 IV
# 분류 : 구현, 그래프 이론, 그래프 탐색

import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
if N == 1:
    for a in arr:
        print(''.join(a))
elif N % 2 == 0:
    for _ in range(R):
        print('O' * C)
else:
    temp = [['O'] * C for _ in range(R)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    def bomb(a, b):
        for i in range(R):
            for j in range(C):
                if a[i][j] == 'O':
                    b[i][j] = '.'
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if 0 <= x < R and 0 <= y < C:
                            b[x][y] = '.'
    bomb(arr, temp)
    if N % 4 == 3:
        for t in temp:
            print(''.join(t))
    else:
        arr = [['O'] * C for _ in range(R)]
        bomb(temp, arr)
        for a in arr:
            print(''.join(a))