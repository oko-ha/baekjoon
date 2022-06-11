# https://www.acmicpc.net/problem/9084
# 이름 : 동전
# 번호 : 9084
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 배낭 문제

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [1] + [0] * (M)
    for c in coin:
        for i in range(c, M + 1):
            dp[i] += dp[i - c]
    print(dp[-1])