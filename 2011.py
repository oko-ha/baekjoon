# https://www.acmicpc.net/problem/2011
# 이름 : 암호코드
# 번호 : 2011
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

s = input().strip()
if s[0] == '0':
    print(0)
else:
    dp = [1, 1] + [0] * (len(s) - 1)
    for i in range(1, len(s)):
        if 0 < int(s[i]) < 10:
            dp[i + 1] += dp[i]
        if 9 < int(s[i-1]) * 10 + int(s[i]) < 27:
            dp[i + 1] += dp[i - 1]
    print(dp[-1] % 1000000)