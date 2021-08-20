# https://www.acmicpc.net/problem/5373
# 이름 : 큐빙
# 번호 : 5373
# 난이도 : 플레티넘 V
# 분류 : 구현, 시뮬레이션

import sys
input = sys.stdin.readline
color = ['w', 'y', 'r', 'o', 'g', 'b']
def swap_right(arr):
    temp = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[j][2 - i] = arr[i][j]
    return temp
def swap_left(arr):
    temp = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[2 - j][i] = arr[i][j]
    return temp
def rotate_UD(a, b, c, d):
    for i in range(3):
        temp = cube[a][0][i]
        cube[a][0][i] = cube[b][0][i]
        cube[b][0][i] = cube[c][2][2-i]
        cube[c][2][2-i] = cube[d][2][2-i]
        cube[d][2][2-i] = temp
def rotate_LRFB(a, b, c, d, e):
    for i in range(3):
        temp = cube[a][i][e]
        cube[a][i][e] = cube[b][i][e]
        cube[b][i][e] = cube[c][e][2-i]
        cube[c][e][2-i] = cube[d][i][e]
        cube[d][i][e] = temp
def rotate(check):
    if check == 'U+':
        rotate_UD(4, 2, 5, 3)
        cube[0] = swap_right(cube[0])
    elif check == 'U-':
        rotate_UD(2, 4, 3, 5)
        cube[0] = swap_left(cube[0])
    elif check == 'D+':
        rotate_UD(3, 5, 2, 4)
        cube[1] = swap_right(cube[1])
    elif check == 'D-':
        rotate_UD(5, 3, 4, 2)
        cube[1] = swap_left(cube[1])
    elif check == 'L+':
        rotate_LRFB(0, 3, 1, 2, 0)
        cube[4] = swap_right(cube[4])
    elif check == 'L-':
        rotate_LRFB(0, 2, 1, 3, 0)
        cube[4] = swap_left(cube[4])
    elif check == 'R+':
        rotate_LRFB(0, 2, 1, 3, 2)
        cube[5] = swap_right(cube[5])
    elif check == 'R-':
        rotate_LRFB(0, 3, 1, 2, 2)
        cube[5] = swap_left(cube[5])
    elif check == 'F+':
        rotate_LRFB(1, 5, 0, 4, 2)
        cube[2] = swap_right(cube[2])
    elif check == 'F-':
        rotate_LRFB(1, 4, 0, 5, 2)
        cube[2] = swap_left(cube[2])
    elif check == 'B+':
        rotate_LRFB(1, 4, 0, 5, 0)
        cube[3] = swap_right(cube[3])
    elif check == 'B-':
        rotate_LRFB(1, 5, 0, 4, 0)
        cube[3] = swap_left(cube[3])
for _ in range(int(input())):
    cube = [[[color[i]] * 3 for _ in range(3)] for i in range(6)]
    n = int(input())
    for cmd in list(input().split()):
        rotate(cmd)
    for i in range(3):
        print(''.join(cube[0][i]))