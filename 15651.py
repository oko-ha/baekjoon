# https://www.acmicpc.net/problem/15651
# 이름 : N과 M (3)
# 번호 : 15651
# 난이도 : 실버 III
# 분류 : 백트래킹

import sys
n, m = map(int, sys.stdin.readline().split())
ans = []
def backtrack(n, m):
    if m > 0:
        for i in range(n):
            ans.append(i + 1)
            backtrack(n, m - 1)
            ans.pop()
    else:
        print(' '.join(map(str, ans)))
backtrack(n, m)

# import itertools
# import sys
# n, m = map(int, sys.stdin.readline().split())
# for i in list(itertools.product([i for i in range(1, n + 1)], repeat=m)):
#     print(' '.join(map(str, i)))