# https://www.acmicpc.net/problem/2617
# 이름 : 구슬 찾기
# 번호 : 2617
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 플로이드-워셜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    dp[a-1][b-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[i][k] and dp[k][j]:
                dp[i][j] = 1
ans = 0
for i in range(N):
    a = b = 0
    for j in range(N):
        a += dp[i][j]
        b += dp[j][i]
    if a > N // 2 or b > N // 2:
        ans += 1
print(ans)