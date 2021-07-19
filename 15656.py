# https://www.acmicpc.net/problem/15656
# 이름 : N과 M (7)
# 번호 : 15656
# 난이도 : 실버 III
# 분류 : 백트래킹

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
def backtracking(k):
    if k < M:
        for a in arr:
            ans.append(a)
            backtracking(k + 1)
            ans.pop()
    else:
        print(' '.join(map(str, ans)))
backtracking(0)