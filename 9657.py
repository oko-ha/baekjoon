# https://www.acmicpc.net/problem/9657
# 이름 : 돌 게임 3
# 번호 : 9657
# 난이도 : 실버 III
# 분류 : 다이나믹 프로그래밍, 게임 이론

import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 1, 0, 1, 1] + [1] * (N - 4)
for i in range(5, N + 1):
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
        dp[i] = 0
print('SK' if dp[N] else 'CY')