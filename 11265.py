# https://www.acmicpc.net/problem/11265
# 이름 : 끝나지 않는 파티
# 번호 : 11265
# 난이도 : 골드 V
# 분류 : 그래프 이론, 플로이드-워셜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

floyd()
for _ in range(M):
    A, B, C = map(int, input().split())
    if dp[A-1][B-1] > C:
        print('Stay here')
    else:
        print('Enjoy other party')