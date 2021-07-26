# https://www.acmicpc.net/problem/15663
# 이름 : N과 M (9)
# 번호 : 15663
# 난이도 : 실버 II
# 분류 : 백트래킹

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
check = [True] * N
ans = []
def backtracking(k):
    if k < M:
        overlap = 0
        for i in range(N):
            if check[i] and overlap != arr[i]:
                overlap = arr[i]
                check[i] = False
                ans.append(arr[i])
                backtracking(k + 1)
                check[i] = True
                ans.pop()
    else:
        print(*ans)
backtracking(0)