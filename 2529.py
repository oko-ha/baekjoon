# https://www.acmicpc.net/problem/2529
# 이름 : 부등호
# 번호 : 2529
# 난이도 : 실버 II
# 분류 : 브루트포스 알고리즘, 백트래킹

import sys
input = sys.stdin.readline
n = int(input())
sign = list(input().split())
check = [True] * 10
stack = []
ans = []
def backtracking(k):
    if k == 0:
        for i in range(10):
            stack.append(i)
            check[i] = False
            backtracking(k + 1)
            stack.pop()
            check[i] = True
    elif k <= n:
        for i in range(10):
            if check[i] and eval(str(stack[-1]) + sign[k - 1] + str(i)):
                stack.append(i)
                check[i] = False
                backtracking(k + 1)
                stack.pop()
                check[i] = True
    else:
        ans.append(''.join(map(str, stack)))
backtracking(0)
print(max(ans))
print(min(ans))