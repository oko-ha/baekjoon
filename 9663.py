# https://www.acmicpc.net/problem/9663
# 이름 : N-Queen
# 번호 : 9663
# 난이도 : 골드 V
# 분류 : 브루트포스 알고리즘, 백트래킹

import sys
n = int(sys.stdin.readline().rstrip())
stack = []
def isQ(i, k):
    for s in range(len(stack)):
        if i == stack[s] or k - s == abs(i - stack[s]):
            return False
    return True
def nQueen(k):
    if k < n:
        ans = 0
        for i in range(n):
            if isQ(i, k):
                stack.append(i)
                ans += nQueen(k + 1)
                stack.pop()
        return ans
    else:
        return 1
print(nQueen(0))