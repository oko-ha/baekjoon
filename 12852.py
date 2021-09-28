# https://www.acmicpc.net/problem/12852
# 이름 : 1로 만들기 2
# 번호 : 12852
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
N = int(sys.stdin.readline())
dp = [0, 0, 1, 1] + [0] * (N - 3)
d = {2:1, 3:1}
for i in range(4, N + 1):
    dp[i] = dp[i - 1] + 1
    d[i] = i - 1
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        d[i] = i // 2
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        d[i] = i // 3
print(dp[N])
temp = N
while temp > 1:
    print(temp, end=' ')
    temp = d[temp]
print(1)