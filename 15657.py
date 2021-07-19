# https://www.acmicpc.net/problem/15657
# 이름 : N과 M (8)
# 번호 : 15657
# 난이도 : 실버 III
# 분류 : 백트래킹

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
def backtracking(k, a):
    if k < M:
        for i in range(a, N):
            ans.append(arr[i])
            backtracking(k + 1, i)
            ans.pop()
    else:
        print(' '.join(map(str, ans)))
backtracking(0, 0)