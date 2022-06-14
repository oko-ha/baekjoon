# https://www.acmicpc.net/problem/1389
# 이름 : 케빈 베이컨의 6단계 법칙
# 번호 : 1389
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-와샬

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    dp[A-1][B-1] = 1
    dp[B-1][A-1] = 1
for k in range(N):
    dp[k][k] = 0
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
ans = (0, INF)
for i, d in enumerate(map(sum, dp)):
    if ans[1] > d:
        ans = (i + 1, d)
print(ans[0])