# https://www.acmicpc.net/problem/2293
# 이름 : 동전 1
# 번호 : 2293
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [1] + [0 for _ in range(k)] 
number = []
for _ in range(n):
    number.append(int(input()))
for num in number:
    for i in range(num, k + 1):
        dp[i] += dp[i - num]
print(dp[k])