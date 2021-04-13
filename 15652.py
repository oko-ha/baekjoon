# https://www.acmicpc.net/problem/15652
# 이름 : N과 M (4)
# 번호 : 15652
# 난이도 : 실버 III
# 분류 : 백트래킹

import sys
n, m = map(int, sys.stdin.readline().split())
ans = []
def backtrack(n, m, x):
    if m > 0:
        for i in range(x, n):
            ans.append(i + 1)
            backtrack(n, m - 1, i)
            ans.pop()
    else:
        print(' '.join(map(str, ans)))
backtrack(n, m, 0)

# import itertools
# import sys
# n, m = map(int, sys.stdin.readline().split())
# for i in list(itertools.combinations_with_replacement([i for i in range(1, n + 1)], m)):
#     print(' '.join(map(str, i)))