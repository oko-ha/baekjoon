# https://www.acmicpc.net/problem/15665
# 이름 : N과 M (11)
# 번호 : 15665
# 난이도 : 실버 II
# 분류 : 백트래킹

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
def backtracking(k):
    if k < M:
        overlap = 0
        for i in range(N):
            if overlap != arr[i]:
                overlap = arr[i]
                ans.append(arr[i])
                backtracking(k + 1)
                ans.pop()
    else:
        print(*ans)
backtracking(0)