# https://www.acmicpc.net/problem/15649
# 이름 : N과 M (1)
# 번호 : 15649
# 난이도 : 실버 III
# 분류 : 

def backtrack(n, m, a, c):
    ans = ''
    if m > 0:
        for i in range(n):
            if c[i]:
                c[i] = False
                print(a[i] + ' ')
                backtrack(n, m - 1, a, c)
                c[i] = True
    else:
        print()

import sys
n, m = map(int, sys.stdin.readline().split())
a = [str(i) for i in range(n, 0, -1)]
c = [True] * n
backtrack(n, m, a, c)