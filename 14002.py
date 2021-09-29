# https://www.acmicpc.net/problem/14002
# 이름 : 가장 긴 증가하는 부분 수열 4
# 번호 : 14002
# 난이도 : 골드 IV
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
ans = 1
d = {}
for i in range(N - 2, -1, -1):
    for j in range(i, N):
        if arr[i] < arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            d[i] = j
            ans = max(ans, dp[i])
print(ans)
for i in range(N):
    if dp[i] == ans:
        temp = i
        for _ in range(ans - 1):
            print(arr[temp], end=' ')
            temp = d[temp]
        print(arr[temp])
        break