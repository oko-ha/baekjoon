# https://www.acmicpc.net/problem/1780
# 이름 : 종이의 개수
# 번호 : 1780
# 난이도 : 실버 II
# 분류 : 분할 정복, 재귀

import sys
n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [0] * 3
def paper(x, y, n):
    color = arr[y][x]
    for i in range(y, n + y):
        for j in range(x, n + x):
            if arr[i][j] != color:
                # 9번 분할
                for a in range(3):
                    for b in range(3):
                        paper(x+n//3*a, y+n//3*b, n//3)
                return
    if color == -1:
        ans[0] += 1
    elif color == 0:
        ans[1] += 1
    else:
        ans[2] += 1
paper(0, 0, n)
print('\n'.join(map(str, ans)))