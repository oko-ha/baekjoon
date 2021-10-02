# https://www.acmicpc.net/problem/9252
# 이름 : LCS 2
# 번호 : 9252
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
A = input().strip()
B = input().strip()
dp = [[''] * (len(B) + 1) for _ in range(len(A) + 1)]
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i + 1][j + 1] = dp[i][j] + A[i]
        else:
            if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                dp[i + 1][j + 1] = dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
if dp[-1][-1]:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
else:
    print(0)