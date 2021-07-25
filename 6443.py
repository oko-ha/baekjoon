# https://www.acmicpc.net/problem/6443
# 이름 : 애너그램
# 번호 : 6443
# 난이도 : 골드 IV
# 분류 : 수학, 문자열, 조합론, 백트래킹

import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    arr = sorted(list(input().strip()))
    check = [True] * len(arr)
    ans = []
    def backtracking(k):
        if k < len(arr):
            overlap = ''
            for i in range(len(arr)):
                if check[i] and overlap != arr[i]:
                    overlap = arr[i]
                    check[i] = False
                    ans.append(arr[i])
                    backtracking(k + 1)
                    check[i] = True
                    ans.pop()
        else:
            print(''.join(ans))
    backtracking(0)