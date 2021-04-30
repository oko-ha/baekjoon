# https://www.acmicpc.net/problem/9184
# 이름 : 신나는 함수 실행
# 번호 : 9184
# 난이도 : 실버 II
# 분류 : 다이나믹 프로그래밍, 재귀

import sys
funcW = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif funcW[a][b][c]:
        return funcW[a][b][c]
    elif a < b < c:
        funcW[a][b][c-1] = w(a, b, c-1)
        funcW[a][b-1][c-1] = w(a, b-1, c-1)
        funcW[a][b-1][c] = w(a, b-1, c)
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        funcW[a-1][b][c] = w(a-1, b, c)
        funcW[a-1][b-1][c] = w(a-1, b-1, c)
        funcW[a-1][b][c-1] = w(a-1, b, c-1)
        funcW[a-1][b-1][c-1] = w(a-1, b-1, c-1)
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))