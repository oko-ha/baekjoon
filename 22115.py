# https://www.acmicpc.net/problem/22115
# 이름 : 창영이와 커피
# 번호 : 22115
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 배낭 문제

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coffee = list(map(int, input().split()))
if K > sum(coffee):
    print(-1)
else:
    dp = [N + 1] * (K + 1)
    dp[0] = 0
    for c in coffee:
        for i in range(K, c - 1, - 1):
            dp[i] = min(dp[i], dp[i - c] + 1)
    print(dp[-1] if dp[-1] < N + 1 else -1)