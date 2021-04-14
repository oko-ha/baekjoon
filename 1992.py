# https://www.acmicpc.net/problem/1992
# 이름 : 쿼드트리
# 번호 : 1992
# 난이도 : 실버 I
# 분류 : 분할 정복, 재귀

import sys
n = int(sys.stdin.readline().rstrip())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
def quadTree(x, y, n):
    num = arr[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if num != arr[i][j]:
                print('(', end='')
                quadTree(x, y, n // 2)
                quadTree(x + n // 2, y, n // 2)
                quadTree(x, y + n // 2, n // 2)
                quadTree(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if num == '1':
        print('1', end='')
    else:
        print('0', end='')
quadTree(0, 0, n)