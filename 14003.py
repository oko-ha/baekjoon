# https://www.acmicpc.net/problem/14003
# 이름 : 가장 긴 증가하는 부분 수열 5
# 번호 : 14003
# 난이도 : 플래티넘 V
# 분류 : 이분 탐색, 가장 긴 증가하는 부분 수열: o(n log n)

import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [-float('inf')]
d = []
for a in A:
    if dp[-1] < a:
        dp.append(a)
        d.append(len(dp) - 1)
    else:
        b = bisect_left(dp, a)
        dp[b] = a
        d.append(b)
temp = len(dp) - 1
ans = []
print(temp)
for i in range(N - 1, -1, -1):
    if d[i] == temp:
        ans.append(A[i])
        temp -= 1
    if temp < 1:
        break
ans.reverse()
print(*ans)