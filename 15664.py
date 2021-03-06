# https://www.acmicpc.net/problem/15664
# 이름 : N과 M (10)
# 번호 : 15664
# 난이도 : 실버 II
# 분류 : 백트래킹

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
def backtracking(k, x):
    if k < M:
        overlap = 0
        for i in range(x, N):
            if  overlap != arr[i]:
                overlap = arr[i]
                ans.append(arr[i])
                backtracking(k + 1, i + 1)
                ans.pop()
    else:
        print(*ans)
backtracking(0, 0)