# https://www.acmicpc.net/problem/7570
# 이름 : 줄 세우기
# 번호 : 7570
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(N):
    c = arr[i]
    dp[c] = dp[c - 1] + 1
print(N - max(dp))