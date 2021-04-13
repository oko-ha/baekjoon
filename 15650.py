# https://www.acmicpc.net/problem/15650
# 이름 : N과 M (2)
# 번호 : 15650
# 난이도 : 실버 III
# 분류 : 백트래킹

import sys
n, m = map(int, sys.stdin.readline().split())
ans = []
check = [True] * n
def backtrack(n, m, x):
    if m > 0:
        for i in range(x, n):
            if check[i]:
                check[i] = False
                ans.append(i + 1)
                backtrack(n, m - 1, i + 1)
                ans.pop()
                check[i] = True
    else:
        print(' '.join(map(str, ans)))
backtrack(n, m, 0)

# from itertools import combinations
# import sys
# n, m = map(int, sys.stdin.readline().split())
# for i in list(combinations([i for i in range(1, n + 1)], m)):
#     print(' '.join(map(str, i)))