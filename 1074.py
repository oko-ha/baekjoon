# https://www.acmicpc.net/problem/1074
# 이름 : Z
# 번호 : 1074
# 난이도 : 실버 I
# 분류 : 분할 정복, 재귀

def blockZ(n, r, c):
    if n > 0:
        num = 0
        if r >= 2 ** n:
            r -= 2 ** n
            num += 2 ** (2 * n + 1)
        if c >= 2 ** n:
            c -= 2 ** n
            num += 4 ** n
        return num + blockZ(n - 1, r, c)
    else:
        return 0

import sys
n, r, c = map(int, sys.stdin.readline().split())
z = [[0, 1], [2, 3]]
print(z[r % 2][c % 2] + blockZ(n - 1, r, c))

# # for loop ver
# import sys
# n, r, c = map(int, sys.stdin.readline().split())
# z = [[0, 1], [2, 3]]
# num = 0
# for i in range(n - 1, 0, -1):
#     if r >= 2 ** i:
#         r -= 2 ** i
#         num += 2 ** (2 * i + 1)
#     if c >= 2 ** i:
#         c -= 2 ** i
#         num += 4 ** i
# print(z[r % 2][c % 2] + num)