# https://www.acmicpc.net/problem/1106
# 이름 : 호텔
# 번호 : 1106
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 배낭 문제

import sys
input = sys.stdin.readline
INF = sys.maxsize

C, N = map(int, input().split())
city = sorted([tuple(map(int, input().split())) for _ in range(N)])
dp = [0] + [INF] * (C + 100)
for a, b in sorted(city):
    for i in range(b, len(dp)):
        dp[i] = min(dp[i], dp[i - b] + a)
print(min(dp[C:]))