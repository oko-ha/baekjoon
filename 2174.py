# https://www.acmicpc.net/problem/2174
# 이름 : 로봇 시뮬레이션
# 번호 : 2174
# 난이도 : 골드 V
# 분류 : 구현, 시뮬레이션

import sys
input = sys.stdin.readline
A, B = map(int, input().split())
arr = [[0] * A for _ in range(B)]
N, M = map(int, input().split())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
pos = {'E' : 0, 'N' : 1, 'W' : 2, 'S' : 3}
robot = []
for i in range(N):
    a, b, c = input().split()
    x, y = B - int(b), int(a) - 1
    arr[x][y] = i + 1
    robot.append((x, y, pos[c]))
command = []
for _ in range(M):
    command.append((input().split()))
def simulate():
    for cmd in command:
        a, b, c = cmd
        x, y, d = robot[int(a) - 1]
        if b== 'L':
            for _ in range(int(c)):
                d = (d + 1) % 4
        elif b == 'R':
            for _ in range(int(c)):
                d = (d - 1) % 4 
        elif b == 'F':
            arr[x][y] = 0
            for _ in range(int(c)):
                x, y = x + dx[d], y + dy[d]
                if B <= x or x < 0 or A <= y or y < 0:
                    return 'Robot {} crashes into the wall'.format(a)
                elif arr[x][y] != 0:
                    return 'Robot {} crashes into robot {}'.format(a, arr[x][y])
            arr[x][y] = int(a)
        robot[int(a) - 1] = (x, y, d)
    return 'OK'
print(simulate())