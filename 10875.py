# https://www.acmicpc.net/problem/10875
# 이름 : 뱀
# 번호 : 10875
# 난이도 : 플레티넘 V
# 분류 : 구현, 시뮬레이션

import sys
input = sys.stdin.readline
L = int(input())
N = 2 * L + 1
cmd = []
for _ in range(int(input())):
    t, d = input().split()
    cmd.append((int(t), {'L':-1, 'R':1}[d]))
cmd.append((N, 0))
vert, hori = [(0, N, -1), (0, N, N)], [(0, N, -1), (0, N, N), (L, L, L)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def start():
    ans = 1
    flag = False
    x, y, direction = L, L, 0
    for t, d in cmd:
        if direction % 2 == 0:
            temp = float('inf')
            nx = x + dx[direction] * t
            minX, maxX = min(x, nx), max(x, nx)
            for a, b, c in hori[:-1]:
                if a <= y <= b and minX <= c <= maxX:
                    flag = True
                    temp = min(abs(c - x) - 1, temp)
            if flag:
                return ans + temp
            else:
                ans += t
                x = nx
                vert.append((minX, maxX, y))
        else:
            temp = float('inf')
            ny = y + dy[direction] * t
            minY, maxY = min(y, ny), max(y, ny)
            for a, b, c in vert[:-1]:
                if a <= x <= b and minY <= c <= maxY:
                    flag = True
                    temp = min(abs(c - y) - 1, temp)
            if flag:
                return ans + temp
            else:
                ans += t
                y = ny
                hori.append((minY, maxY, x))
        direction = (direction + d) % 4
    return ans
print(start())