# https://www.acmicpc.net/problem/2580
# 이름 : 스도쿠
# 번호 : 2580
# 난이도 : 골드 IV
# 분류 : 백트래킹

import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]
problems = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            problems.append((i, j))
n = len(problems)
def check(a, b):
    for i in range(9):
        if i == a:
            continue
        if sudoku[i][b] == sudoku[a][b]:
            return False

    for i in range(9):
        if i == b:
            continue
        if sudoku[a][i] == sudoku[a][b]:
            return False
    
    c = a // 3 * 3
    d = b // 3 * 3
    for i in range(c, c + 3):
        for j in range(d, d + 3):
            if i == a and j == b:
                continue
            if sudoku[i][j] == sudoku[a][b]:
                return False
    return True

def backtracking(k):
    if k < n:
        x, y = problems[k]
        for i in range(1, 10):
            sudoku[x][y] = i
            if check(x, y):
                backtracking(k + 1)
        sudoku[x][y] = 0
    else:
        for s in sudoku:
            print(*s)
        exit(0)
backtracking(0)